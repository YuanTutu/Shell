#!/bin/bash
find /opt -name 'fastjson*' > fast.txt
sed 's/fastjson-1.2.*.jar//g' fast.txt > sed.txt
for line in `cat sed.txt`
do
#	echo $line
	cp $line/fastjson* /home/hik/
	rm -f $line/fastjson*
	cp /home/hik/fastjson-1.2.70.jar $line
done
