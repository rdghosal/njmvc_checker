#!/usr/bin/bash

# Delete existing version
if [ -d ./njmvc_checker ]; then
	echo "Removing current version of ./njmvc_checker"
	rm -r njmvc_checker
fi

# Copy target files and directories 
mkdir ./njmvc_checker
cp ./app.py \
	./njmvc_checker.py \
   	./njmvc_cron.txt \
	./requirements.txt \
	./entrypoint.sh \
	./init.sh \
	./local.env \
	./njmvc_checker

cp -r ./scraper \
	./email_client \
	./utils \
	./njmvc_checker

# Remove pycache
rm -r ./njmvc_checker/*/*cache*
rm -r ./njmvc_checker/*/.*cache*

# Zip folder
sudo zip -r njmvc_checker.zip njmvc_checker
echo "Completed zipping application as njmvc_checker.zip"

