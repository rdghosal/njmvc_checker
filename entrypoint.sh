#!/usr/bin/bash
BASE_URL=$PWD/app/
source ${BASE_URL}/local.env
/usr/bin/python3 ${BASE_URL}njmvc_checker.py -s "knowledge test" -c "Edison,South Plainfield,Rahway" >> ${BASE_URL}njmvc_checker.log

if grep -qe "Found [0-9]\+ appointments" ${BASE_URL}njmvc_checker.log; then
    echo "Stopping cron..." >> ${BASE_URL}njmvc_checker.log
    /usr/bin/crontab -r
fi