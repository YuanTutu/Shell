#!/bin/bash

cd /home/hik

cat fast.txt |while read LINE

do
	OLD_FASTJOSN=`echo $LINE|awk -F "/" '{print $NF}'`
	
	for i in `ls |grep fastjson`
        
	do
 
	if [ $i = $OLD_FASTJOSN ];then
 	
	OLD_DIR=`dirname $LINE`

	cp $i $OLD_DIR/
	
	fi
	
	done
done
