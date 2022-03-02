#!/bin/bash
#author yuanbo6
#编写目的，简化tcpdump抓包
#更新日志
#20220302 编写此脚本
DATATIME=`date +"%Y%m%d%H%M"`
echo "！！！请认真阅读提示！！！"
echo "抓包结束之后自己按下Ctrl+C终止抓包"
echo "如果输错字符也别慌，Ctrl+backspace删除 即可删掉"
eth_name=$(ip a|grep -v "LOOPBACK"|grep "UP"|awk '{print $2}')
echo "目前网卡有"$eth_name""
echo "如果有docker可能会显示虚拟网桥信息，我们一般只需要基本的ensxxx ethxxx等类似网卡"
read -p "输入你想抓包的网卡>>>" eth
read -p "输入想要过滤的IP>>>" IP
echo "端口过滤条件可以类似 udp port 7100 / udp port 7100 or udp port 5060 等等形式，and or not条件自由组合"
read -p "输入端口过滤条件>>>" port
echo "保存位置需要确定权限允许，一般推荐/home/hik/下面"
echo "输入需要完整输入最后的/，别只输入/home/hik这样"
read -p "输入保存位置，只需要位置，不需要抓包命名>>>" save_path
echo "抓包结束之后自己按下Ctrl+C终止抓包"
echo "抓包会在"${save_path}"路径下生成一个类似 202203021542.pcap 命名的抓包文件"
tcpdump -i $eth host $IP and $port -s 0 -w ${save_path}${DATATIME}.pcap -v
