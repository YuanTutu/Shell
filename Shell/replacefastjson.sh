#!/bin/bash
#作者 袁博6
#更新日志2020年7月写好后一直没有更新，等到2022突然发现还有部分项目有紧急需要，鉴于之前留下的坑点雷点，决定修补一下

PWD=`pwd`
DATATIME=`date +"%Y%m%d%H%M"`
mkdir /home/hik/${DATATIME}/

find /opt -name 'fastjson*' > fastjson_origin_path_${DATATIME}.txt
sed 's/fastjson-1.2.*.jar//g' fastjson_path_${DATATIME}.txt > replace.txt
for line in `cat replace.txt`
do
	cp $line/fastjson* /home/hik/${DATATIME}/
	rm -f $line/fastjson*
	cp /home/hik/fastjson-1.2.70.jar $line
done
rm -rf replace.txt
echo "重启各种组件看看能不能启动"
echo "如果启动失败，需要根据fastjson_origin_path_${DATATIME}.txt中的路径进行手动还原"
echo "备份路径在/home/hik/${DATATIME}/下"