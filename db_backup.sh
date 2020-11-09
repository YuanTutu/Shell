#!/bin/sh
#数据库备份目录
backupdir=/home/hik/backup
#数据库备份文件名称，以时间作为唯一码
data=$(date +%Y%m%d%H%M%S)
echo $data
#备份device_manage数据库
pg_dump "host=11.254.19.56 port=5432 user=postgres password=Hik12345 dbname=imp" -o>$backupdir/back$data.dump
echo sucess!
#删除15天前的备份文件:mmin分钟、mtime天
find $backupdir -mtime +15 -name "*.sql" -exec sudo rm -rf{} \;
