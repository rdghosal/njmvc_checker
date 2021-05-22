#!/usr/bin/bash
source /app/local.env
/usr/bin/python3 /app/njmvc_checker.py -s "knowledge test" -c "Edison,South Plainfield,Rahway" >> /app/njmvc_checker.log

if grep -qe "Found [0-9]\+ appointments" /app/njmvc_checker.log; then
    echo "Stopping cron..." >> /app/njmvc_checker.log
    /usr/sbin/service cron stop
fi