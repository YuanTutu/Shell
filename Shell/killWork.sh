#!/bin/sh
#kill process
kill -9 $(ps -ef|grep work32|grep -v grep|awk '{print $2}')
kill -9 $(ps -ef|grep work32-deamon|grep -v grep|awk '{print $2}')
kill -9 $(ps -ef|grep work64|grep -v grep|awk '{print $2}')
kill -9 $(ps -ef|grep work64-deamon|grep -v grep|awk '{print $2}')
kill -9 $(ps -ef|grep xmr|grep -v grep|awk '{print $2}')

#kill virus file
rm -rf /usr/.work/  
rm -rf /tmp/config.json
rm -rf ./work32-deamon
rm -rf ./work64-deamon
rm -rf /tmp/xmr
rm -rf /usr/.work/work32
rm -rf /usr/.work/work64
rm -rf /tmp/secure.sh
rm -rf /tmp/auth.sh
#clean cron
sed -i -r '/\.work\/work32/d' /var/spool/cron/crontabs/root
sed -i -r '/\.work\/work32/d' /etc/crontab
sed -i -r '/\.work\/work64/d' /var/spool/cron/crontabs/root
sed -i -r '/\.work\/work64/d' /etc/crontab
#delete ssh
sed -i -r '/AAAAB3NzaC1yc2EAAAADAQABAAABAQD/d' /root/.ssh/authorized_keys
#repair
mv /usr/bin/curl1 /usr/bin/curl&mv /usr/bin/wget1 /usr/bin/wget