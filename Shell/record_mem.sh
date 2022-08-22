#!/bin/bash
#nohup sh record_mem.sh &
#author:yuanbo6
#date:20220822

touch /tmp/record_mem.log

while true
do
DATETIME=`date +"%Y%m%d%H%M"`
Mem_total=$(free -g|grep Mem|awk -F " " '{print $2}')
Mem_used=$(free -g|grep Mem|awk -F " " '{print $3}')
Mem_free=$(free -g|grep Mem|awk -F " " '{print $4}')
Mem_buff=$(free -g|grep Mem|awk -F " " '{print $6}')
Swap_total=$(free -g|grep Swap|awk -F " " '{print $2}')
Swap_used=$(free -g|grep Mem|awk -F " " '{print $3}')
Swap_free=$(free -g|grep Mem|awk -F " " '{print $4}')

echo "#################################" >> /tmp/record_mem.log
echo "Now is ${DATETIME}" >> /tmp/record_mem.log
echo "Memory total is ${Mem_total} G..." >> /tmp/record_mem.log
echo "Memory has used ${Mem_used} G..." >> /tmp/record_mem.log
echo "Free space is ${Mem_free} G..." >> /tmp/record_mem.log
echo "Buff cache is ${Mem_buff} G..." >> /tmp/record_mem.log
echo "Swap total is ${Swap_total} G..." >> /tmp/record_mem.log
echo "Swap has used ${Swap_used} G..." >> /tmp/record_mem.log
echo "Free swap is ${Swap_free} G..." >> /tmp/record_mem.log
echo " " >> /tmp/record_mem.log
sleep 10

done
