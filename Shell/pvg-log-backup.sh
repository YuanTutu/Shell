#!/bin/bash

######定期备份pvg log到指定的服务器
######系统需支持sshpass命令
######脚本把最近24小时的log文件打包，上传到备份服务器指定目录
######需要把脚本加到crond定时服务，每天夜里执行
######比如，每天夜里2点执行一次：  0 2 * * * /opt/pvg-log-backup.sh


######配置本地IP, 需要备份的log目录######
localip="11.49.246.25"
dir="/home/netposa/pvg/log"


######配置备份服务器IP，ssh端口，ssh密码，指定备份到哪个目录#####
backip="11.49.246.32"
sshport="22222"
sshpass="Cpxl123"
backdir="/nas/pvg"


backfile="pvg-log-backup-`date +%F_%T`.tar.gz"

tar zcf /tmp/$backfile `find $dir -maxdepth 5 -mtime -1` /root/.bash_history /var/log/wtmp

sshpass -p $sshpass ssh -p $sshport -o ConnectTimeout=5 -o stricthostkeychecking=no root@$backip 'mkdir -p '$backdir'/'$localip''

if [ $? -eq 0 ];then
        sshpass -p $sshpass scp -P $sshport -o ConnectTimeout=5 -o stricthostkeychecking=no /tmp/$backfile root@$backip:$backdir/$localip
else
        echo "backup failed!"
fi

rm -rf /tmp/$backfile
echo "backup sucess!"

