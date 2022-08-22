#!/bin/bash

#快速检测常见系统危险配置

export LANG=en
export IP_ADDR=`/sbin/ip a|grep -v inet6|grep inet|grep -v "127.0.0.1"|awk '{print $2}'|awk -F / '{print $1}'|head -1`
export DATETIME=`date +"%Y%m%d%H%M"`
export FILE_NAME=${IP_ADDR}_${DATETIME}.txt
export FILE_PATH=/tmp
export FILE_RESULT=${FILE_PATH}/${FILE_NAME}

touch ${FILE_RESULT}
os_user=$(whoami)



#判断当前执行脚本的用户是否为root
check_root() {
  if [ "${os_user}" != "root" ]; then
    echo "请在root用户下执行本脚本！" && echo "参考命令：su - root" && exit 0
  else
    echo "#############################################"
    echo "当前执行用户是root，校验正确开始进行安全检测"
    echo "#############################################"
    echo ""
  fi

}

#时区检测
check_timezone(){
        timezone=$(timedatectl status|grep zone|awk -F : '{print $2}'|cut -d " " -f 2)
        true_timezone="Asia/Shanghai"
        echo "当前系统时区为：${timezone}" >> ${FILE_RESULT}
        echo "标准时区为：${true_timezone}" >> ${FILE_RESULT}
        if [ "${timezone}" == "${true_timezone}" ];then
                echo "时区设置正确，是东八区" >> ${FILE_RESULT}
        else
                echo "时区不是东八区，请及时修正" >> ${FILE_RESULT}
        fi
		echo " " >> ${FILE_RESULT}
}

#指令工具检测
command_check(){
	echo "*****检测工具指令是否安装*****" >> ${FILE_RESULT}
	lsof_status=$(rpm -qa|grep losf)
	netstat_status=$(rpm -qa|grep net-tools)
	echo "待检测端口为22 5500 8068 9200 11211" >> ${FILE_RESULT}
	if [ -z $lsof_status ];then
		echo "lsof没有安装,请手动检查端口" >> ${FILE_RESULT}
		echo " " >> ${FILE_RESULT}
	else
		check_sshport
	fi
	if [ -z $netstat_status ];then
		echo "netstat没有安装,请手动检查端口" >> ${FILE_RESULT}
		echo " " >> ${FILE_RESULT}
	else
		check_other_ports
	fi
}

# 常见危险端口检测
check_sshport() {
	echo "*****开始检测端口*****" >> ${FILE_RESULT}
	ssh_port=$(lsof -i:22)
	if [ -z "$ssh_port" ];then
		echo "22 没有被占用" >> ${FILE_RESULT}
	else
		echo "请复查一下22端口占用情况，是否为ssh端口，如果是ssh端口请尽快修改" >> ${FILE_RESULT}
	fi
}
check_other_ports() {
	dangerous_ports="5500 8068 9200 11211"
	netstat_info=$(netstat -tlnp|grep tcp|awk '{print $4}'|cut -d: -f 2)
	for port in $dangerous_ports
	do
		flag=$(echo $netstat_info|grep $port)
		#echo $flag
		if [ -z "$flag" ];then #-z 检测字符串长度是否为0，为0返回 true。
			echo "$port 没有被占用" >> ${FILE_RESULT}
		else
			echo "$port 正在被占用，请检查你的防火墙配置，关闭外部访问" >> ${FILE_RESULT}
		fi
	done
	echo " " >> ${FILE_RESULT}
}

# 检测防火墙开启关闭状态
check_firewall() {
	echo "*****开始检测防火墙运行状态*****" >> ${FILE_RESULT}
	firewall_status=$(systemctl status firewalld|grep running|awk '{print $3}'|cut -d "(" -f 2|cut -d ")" -f 1)
	if [ -z "firewall_status" ];then
		echo "请打开防火墙！！！" >> ${FILE_RESULT}
	else
		echo "防火墙正在运行，systemctl status firewalld检测为running" >> ${FILE_RESULT}
	fi
	echo " " >> ${FILE_RESULT}
}

# 检测ssh相关配置项
check_ssh() {
	echo "*****开始检测ssh的配置项*****" >> ${FILE_RESULT}
	PermitRootLoginStatus=$(cat /etc/ssh/sshd_config|grep PermitRootLogin|grep -E "yes|no")
	echo "配置文件中，是否允许root直接登录的配置为： $PermitRootLoginStatus" >> ${FILE_RESULT}
	echo "如果不是PermitRootLogin no，请修改，或者去掉注释并重启ssh" >> ${FILE_RESULT}
	#cat /etc/ssh/sshd_config|grep PermitRootLogin|grep -v ^#|cut -d " " -f 2  #得到结果是no是禁止root登录
	PermitRootLoginNo=$(cat /etc/ssh/sshd_config|grep PermitRootLogin|grep -v ^#|cut -d " " -f 2)
	if [ -z $PermitRootLoginNo ];then
		echo "当前系统可能允许root直接ssh登录，请及时修改！！！" >> ${FILE_RESULT}
	else
		echo "当前系统禁止root直接ssh登录" >> ${FILE_RESULT}
	fi
	echo "配置文件路径：/etc/ssh/sshd_config" >> ${FILE_RESULT}
	echo " " >> ${FILE_RESULT}
}

# USEPAM是否开启
check_usepam() {
	echo "*****开始检测UsePAM配置项*****" >> ${FILE_RESULT}
	UsePAMStatus=$(cat /etc/ssh/sshd_config|grep -v ^#|grep UsePAM|cut -d " " -f 2|grep yes)
	#echo $UsePAMStatus
	if [[ $UsePAMStatus = "yes" ]];then
		echo "UsePAM 已开启" >> ${FILE_RESULT}
	else
		echo "UsePAM 未开启，建议开启并配置各种pam参数" >> ${FILE_RESULT}
		echo "配置文件路径：/etc/ssh/sshd_config" >> ${FILE_RESULT}
	fi
	echo " " >> ${FILE_RESULT}
}
# 密码多次输入错误锁定配置，需要配合PAM，比较麻烦

# 锁定用户，解锁用passwd -u UserName  暂时没想好锁定有啥用
lock_user_password(){
	echo "开始锁定用户..."
	for i in `cat /etc/shadow|egrep '!|\*'|awk -F ":" '{print $1}'`
	do
	passwd -l $i > /dev/null  2>&1 && echo $i锁定已完成 
	done
	echo " "
}

#检测超级用户权限账号
check_super_user() {
	echo "*****开始检测root权限用户*****" >> ${FILE_RESULT}
	suser=$(cat /etc/passwd|cut -d : -f 1,3|grep :0|awk -F ":" '{print $1}')
	echo "具有root权限的账号有：${suser}" >> ${FILE_RESULT}
	count_suser=`cat /etc/passwd|cut -d : -f 1,3|grep :0|awk -F ":" '{print $1}'|wc -l`
	if [[ ${count_suser} -eq 1 ]];then
		echo "只有root账号具有root权限，账号权限正确" >> ${FILE_RESULT}
	else
		echo "有多个用户具有root权限，请及时处理，关闭非必要权限" >> ${FILE_RESULT}
	fi
	echo " " >> ${FILE_RESULT}
}

#检测用户超时300秒自动退出配置
time_out(){
	echo "*****开始检测超时退出配置*****" >> ${FILE_RESULT}
	time=`cat /etc/profile|grep -v ^#|grep TMOUT|awk -F "=" '{print $2}'`
	if [[ ${time} -lt 300 ]];then
		echo "超时配置低于300秒，请修改此配置" >> ${FILE_RESULT}
		echo "/etc/profile添加export TMOUT=300并source /etc/profile" >> ${FILE_RESULT}
	else
		echo "超时配置大于等于300秒，无需处理" >> ${FILE_RESULT}
	fi
	echo " " >> ${FILE_RESULT}
}

# 密码有效期相关检测
passwd_policy(){
	echo "*****开始检测密码有效期相关配置*****" >> ${FILE_RESULT}
	max_day=`cat /etc/login.defs |grep PASS_MAX_DAYS|grep -v ^#|awk -F " " '{print $2}'`
	min_day=`cat /etc/login.defs |grep PASS_MIN_DAYS|grep -v ^#|awk -F " " '{print $2}'`
	min_len=`cat /etc/login.defs |grep PASS_MIN_LEN|grep -v ^#|awk -F " " '{print $2}'`
	warn_age=`cat /etc/login.defs |grep PASS_WARN_AGE|grep -v ^#|awk -F " " '{print $2}'`
	if [[ ${max_day} -gt 180 ]];then
		echo "密码最长有效期超过180天，请及时修改" >> ${FILE_RESULT}
	fi
	if [[ ${min_day} -eq 0 ]];then
		echo "密码最小修改间隔为0天，按需修改" >> ${FILE_RESULT}
	fi
	if [[ ${min_len} -lt 8 ]];then
		echo "密码最小长度小于8，请及时修改" >> ${FILE_RESULT}
	fi
	echo "密码过期提醒为${warn_age}天，按需修改" >> ${FILE_RESULT}
	echo "配置文件路径：/etc/login.defs" >> ${FILE_RESULT}
	echo " " >> ${FILE_RESULT}
}

# 关键文件权限状态
file_auth(){
	echo "*****开始检测关键文件权限*****" >> ${FILE_RESULT}
	passwd_auth=$(ls -l /etc/passwd|awk -F " " '{ print $1 }')
	group_auth=$(ls -l /etc/group|awk -F " " '{ print $1 }')
	shadow_auth=$(ls -l /etc/shadow|awk -F " " '{ print $1 }')
	service_auth=$(ls -l /etc/services|awk -F " " '{ print $1 }')
	security_auth=$(ls -l /etc|grep security|awk -F " " '{ print $1 }')
	echo "passwd文件权限为：${passwd_auth},推荐权限为rw-r--r--即644" >> ${FILE_RESULT}
	echo "group文件权限为：${group_auth},推荐权限为rw-r--r--即644" >> ${FILE_RESULT}
	echo "shadow文件权限为：${shadow_auth},推荐权限为---------即000" >> ${FILE_RESULT}
	echo "service文件权限为：${service_auth},推荐权限为rw-r--r--即644" >> ${FILE_RESULT}
	echo "security文件夹权限为：${security_auth},推荐权限为rw-------即600" >> ${FILE_RESULT}
	echo "如需修改自行使用chmod修改" >> ${FILE_RESULT}
	echo "注意security只修改文件夹本体，不修改内部内容，不要加R" >> ${FILE_RESULT}
	echo " " >> ${FILE_RESULT}
}

#centos7.x关闭不必要的服务
close_service_7(){
	echo "####################################"
	echo "开始关闭不需要的服务..."
	for i in "postfix.service bluetooth.target"
	do
	echo "关闭$i"
	systemctl stop $i
	systemctl disable $i
	done
	echo "关闭服务已完成"
	echo "###################################"
	echo " "
}

close_shell(){
	echo "###################################" >> ${FILE_RESULT}
	echo "##########安全性检查完成###########" >> ${FILE_RESULT}
	echo "##########系统安全无小事###########" >> ${FILE_RESULT}
	echo "###################################" >> ${FILE_RESULT}
}


tishi(){
echo "*****提示*****" 
echo "如需三级等保加固请使用加固脚本集中处理"
echo "/产品资料/02.系统业务/共享软件研发中心/02 共享软件/11.系统支持/01技术类/02操作系统/Linux/CentOS/脚本工具/三级等保加固"
echo "当前执行结果已经输出在/tmp路径下，按需自取"
}

check_root
check_timezone
command_check
check_firewall
check_ssh
check_usepam
#lock_user_password
check_super_user
time_out
passwd_policy
file_auth
close_shell
tishi
