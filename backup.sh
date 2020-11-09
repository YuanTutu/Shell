#!/bin/bash
#ls
export PATH=$PATH:/usr/pgsql-9.4/bin/
read -p "请输入数据库ip: " HOST
read -p "请输入数据库的端口号：" PORT
read -p "请输入数据库用户名：" USERNAME
read -p "请输入数据库密码：" PASSWORD
read -p "请输入备份数据库路径：" PGPATH
echo "start back pg...."
pg_dump "host=$HOST port=$PORT user=$USERNAME password=$PASSWORD dbname=cascade" -Fc -b -f "$PGPATH"
echo "back up pg suss."

