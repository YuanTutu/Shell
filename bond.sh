#!/bin/sh
# --------------------------------------------------
#
# @author yangxiao
# @date 2018-06-20 创建脚本，默认所有网卡做聚合
# @date 2018-06-21 修改脚本，新增网卡选择，针对选择网卡做聚合
# @date 2018-06-22 修改脚本，新增配置网卡开机自启动
# --------------------------------------------------
#
echo "欢迎使用网卡绑定脚本"

echo "该脚本需在root用户下完成,开始效验用户"

user=`whoami`
if [ "${user}" != "root" ];then
	   echo "请在root用户下执行本脚本！" &&  echo "参考命令：su root" && exit 0
else echo "当前执行用户校验正确！"
fi

net_pwd=/etc/sysconfig/network-scripts

echo "开始清除原有端口聚合配置"
rm -rf ethname.txt
rm -rf ${net_pwd}/*bak
mkdir ${net_pwd}/Bondbak
cp   ${net_pwd}/ifcfg-en* ${net_pwd}/Bondbak/.
mv   ${net_pwd}/*bond*    ${net_pwd}/Bondbak/.
cp -r ${net_pwd}/Bondbak /home/Bondbak-"`date`" 

echo "清除配置已完成"

echo "您将需要输入以下信息完成配置"
echo "----------------------------------------------------"
echo "1-网卡绑定名称，建议为bond0（数字0）"
echo "2-网卡绑定模式,建议为模式6"
echo "3-服务器IP地址,"
echo "4-服务器子网掩码,"
echo "5-服务器网关,"
echo "6-需要绑定的实际网卡名称"
echo "----------------------------------------------------"
while true
do
	read -p "1-网卡绑定名称:" deviceName
     echo "您已经配置绑定名称为: $deviceName"
     echo "2-请选择网卡绑定模式: 0 | 1 | 2 | 3 | 4 | 5 | 6 :"
read -n 1 -p "(Default: type 6): " BondType
     echo 
     case $BondType in
     0)
     echo "您已经选择绑定模式为0 balance-rr."
     BondType=balance-rr
     break;;
     1)
     echo "您已经选择绑定模式为1 active-backup."
     BondType=active-backup
     break;;
     2)
     echo "您已经选择绑定模式为2 balance-xor."
     BondType=balance-xor
     break;;
	 3)
     echo "您已经选择绑定模式为3 broadcast."
     BondType=broadcast
     break;;
	 4)
     echo "您已经选择绑定模式为4 802.3ad."
     BondType=802.3ad
     break;;
	 5)
     echo "您已经选择绑定模式为5 balance-tlb."
     BondType=balance-tlb
     break;;
	 6)
	 echo "您已经选择绑定模式为6 balance-alb."
     BondType=balance-alb
     break;;
     *)
       echo "您已经选择绑定模式为6 balance-alb."
       BondType=balance-alb
      break;;
     esac
done
	 
read -p "3-服务器IP地址:" Ipaddr
     echo "您已经输入设备IP为 : $Ipaddr"
	 
read -p "4-服务器子网掩码:" Netmask
     echo "您已经输入设备子网掩码为: $Netmask"
	 
read -p "5-服务器网关:" Gateway
     echo "您已经输入设备网关为: $Gateway"
	
touch ifcfg-bond0

echo "DEVICE=$deviceName" >> ifcfg-bond0
echo "NAME=$deviceName" >> ifcfg-bond0
echo "BONDING_OPTS=\"miimon=1 updelay=0 downdelay=0 mode=$BondType\"" >> ifcfg-bond0
echo "TYPE=Bond" >> ifcfg-bond0
echo "BONDING_MASTER=yes" >> ifcfg-bond0
echo "BOOTPROTO=none" >> ifcfg-bond0
echo "USERCTL=no" >> ifcfg-bond0
echo "NM_CONTROLLED=no" >> ifcfg-bond0
echo "IPADDR=$Ipaddr" >> ifcfg-bond0
echo "NETMASK=$Netmask" >> ifcfg-bond0
echo "GATEWAY=$Gateway" >> ifcfg-bond0
echo "DEFROUTE=yes" >> ifcfg-bond0
echo "ONBOOT=yes" >> ifcfg-bond0

mv ifcfg-bond0 ${net_pwd}/.

echo "查找当前服务器所有网卡名称:"
echo "--------------------------------"
cat /proc/net/dev |tail -n +3 | awk '{print $1}'
echo "--------------------------------"

echo "6-请输入需要绑定的网卡名称,多个网卡之间用英文空格隔开"
read -p "网卡名称:" ethname

echo "$ethname" >> ethname.txt
sed -i  's/en/ifcfg-en/g' ethname.txt
ethname_new=`cat ethname.txt`

cd ${net_pwd}

#echo "删除网卡配置中不相关项"
sed -i '/DEFROUTE/'d $ethname_new
sed -i '/IPV/'d $ethname_new
sed -i '/PEER/'d $ethname_new
sed -i '/MASTER/'d $ethname_new
sed -i '/UUID=/'d $ethname_new
sed -i '/ONBOOT/'d $ethname_new
sed -i '/IPADDR/'d $ethname_new
sed -i '/NETMASK/'d $ethname_new
sed -i '/GATEWAY/'d $ethname_new
sed -i '/BOOTPROTO/'d  $ethname_new
sed -i '/SLAVE/'d $ethname_new
sed -i '/NM_CONTROLLED/'d $ethname_new
sed -i '/USERCTL/'d $ethname_new

echo "写入以下配置信息到对应网卡中"
echo "--------------------------------"
echo "BOOTPROTO=none" | tee -a $ethname_new
echo "MASTER=$deviceName" | tee -a $ethname_new
echo "SLAVE=yes" | tee -a $ethname_new
echo "NM_CONTROLLED=no" | tee -a $ethname_new
echo "USERCTL=no" | tee -a $ethname_new
echo "ONBOOT=yes" | tee -a $ethname_new
echo "--------------------------------"

systemctl stop NetworkManager
systemctl disable NetworkManager

systemctl restart network




