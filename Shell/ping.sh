#!/bin/bash
# 用于批量ping一些IP并写入ip.txt文件
# 可以看出文件的路径可以自己配置
DATE=$(date +%Y%m%d) 
if 
    [ ! -d /root/$DATE ] 
then 
    mkdir /root/$DATE 
fi 
IPADD=$(cat /root/ip.txt) 
for ip in $IPADD 
do 
    nohup ping $ip -c 10|awk '{print strftime("%c",systime()) "\t"$0}' >>/root/$DATE/$ip.txt& 
done 
