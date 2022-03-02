#!/bin/bash
#作者 袁博
#目的：快速检查服务器内一些基础配置信息
#20220224第一版，根据按键选择想显示的内容
#20220225第二版，不再根据按键选择显示，直接显示所有的内容,更名为check_server_status.sh
#20220301第三版，处理一些输出细节，更利于查看。另外新增对ssh可登录用户和端口的校验.部分变量类似网卡和防火墙需要处理掉前后的符号，没有找到好的合并方法，只能先获取然后用%？再处理一次
#20220302第四版，增加opt文件系统的校验，以及调整排版

#输出
echo "此脚本旨在检测服务器当前基本信息，便于排查问题"
echo "基本信息："

#hostname
host_name=$(hostname)
#输出HOST_NAME
echo "本机hostname为 "${host_name}""
echo "**********"

echo "网络信息（目前只检测单网卡）："
interface_count=$(ip a|grep inet|grep -v inet6|grep -v "127.0.0.1"|awk '{print $2}'|wc -l)
if [[ "${interface_count}" = "1" ]];then
	server_ip=$(ip a|grep inet|grep -v inet6|grep -v "127.0.0.1"|awk '{print $2}')
	eth_name=$(ip a|grep -v "LOOPBACK"|grep "UP"|awk '{print $2}')
	eth_true_name=${eth_name%?}
	eth_link_status=$(ethtool ${eth_true_name}|grep "Link"|awk '{print $3}')
	echo "本机IP为 "${server_ip}""
	echo "网卡目前连接状态为"${eth_link_status}""
	echo "网口速率自行用ethtools工具查看，脚本没写。"
	if [ ${eth_link_status} = "no" ];then
		echo "没有检测到网口连接状态，请检查。"
#	else
#		echo "目前网口接线了"
	fi
elif [[ "${interface_count}" != "1" ]];then
	echo "网卡数量不为1，建议自己用ip a等指令查看配置"
fi
echo "**********"

#文件系统
root_used=$(df -Th|grep root|awk '{print $4}')
root_free=$(df -Th|grep root|awk '{print $5}')
root_file_used_persent=$(df -Th|grep root|awk '{print $6}')
opt_used=$(df -Th|grep opt|awk '{print $4}')
opt_free=$(df -Th|grep opt|awk '{print $5}')
opt_file_used_persent=$(df -Th|grep opt|awk '{print $6}')
echo "文件系统使用情况"
#输出文件系统使用情况
echo "root目前使用了 "${root_used}",剩余 "${root_free}",总体用了 "${root_file_used_persent}""
echo "opt目前使用了 "${opt_used}",剩余 "${opt_free}",总体用了 "${opt_file_used_persent}""
echo "**********"

#CPU状态
cpu_count=$(cat /proc/cpuinfo|grep MHz|wc -l)
cpu_used_persent=$(top -b -n1 | fgrep "Cpu(s)" | tail -1 | awk -F'id,' '{split($1, vs, ","); v=vs[length(vs)];sub(/\s+/, "", v);sub(/\s+/, "", v); printf "%s\n", 100-v; }')
echo "CPU内存磁盘IO情况："
#输出CPU使用情况
echo "CPU共有"${cpu_count}"核,目前使用了"${cpu_used_persent}"%"
#内存状态
mem_count=$(free -m | awk -F '[ :]+' 'NR==2{printf "%d",$3}')
mem_used_persent=$(free -m | awk -F '[ :]+' 'NR==2{printf "%d", ($2-$7)/$2*100}')
#输出内存使用情况
echo "内存使用了"${mem_count}"M,“共计占比"${mem_used_persent}"%"
#硬盘io状态
xda_io_status=$(iostat -d -x 1 1|grep da|awk '{print $14}')
xda_io_int=$(iostat -d -x 1 1|grep da|awk '{print int($14)}')
#输出IO情况
echo "目前第一块磁盘（vda或者sda)繁忙度为"${xda_io_status}"%"
#if [ ${xda_io_int} -ge "0" ];then
#	echo "磁盘IO状态有点高"
#fi
echo "**********"

#防火墙状态
firewalld_status=$(systemctl status firewalld|grep Active|awk '{print $3}')
firewalld_one_status=${firewalld_status:1}
firewalld_final_status=${firewalld_one_status%?}
#ssh配置
p_root_l=$(cat /etc/ssh/sshd_config|grep -v "prohibit"|grep -v "without"|grep "PermitRootLogin"|awk '{print $2}')
ssh_port=$(cat /etc/ssh/sshd_config|grep -v "#"|grep Port|awk '{print $2}')
echo "安全配置："
#输出防火墙开关状态
echo "防火墙目前状态为"${firewalld_final_status}""
if [ ${firewalld_final_status} != "running" ];then
	echo "请检查防火墙状态"
fi
#输出是否允许root登录
echo "目前ssh是否允许root直接登录："${p_root_l}""
if [ ${p_root_l} = "yes" ];then
	echo "允许直接root登录，危险"
fi
#输出ssh端口
echo "目前ssh端口为："${ssh_port}""
if [[ ${ssh_port} = "22" ]];then
	echo "ssh端口是22，请及时修改"
fi
echo "**********"

echo "脚本仅供参考"
