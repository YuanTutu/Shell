#!/bin/bash

STATUS=`service hik.opsmgr.agent.protect status| grep Active | awk '{print $3}' | cut -d "(" -f2 | cut -d ")" -f1`

if [ "$STATUS" == "running" ]
then
	echo `date` "is ok..." >> /home/hik/startagent.log
else
	echo `date` "test protect is not running" >> /home/hik/startagent.log
	cd /opt/hikvision/web/opsMgrAgent/bin/
	./hik.opsmgr.agent.protect start
fi
