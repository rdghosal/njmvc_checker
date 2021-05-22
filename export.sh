#!/usr/bin/bash

# Delete existing version
if [ -d ./app ]; then
	echo "Removing current version of ./njmvc_app"
	rm -r ./app
fi

# Copy target files and directories 
mkdir ./app && mkdir ./app/njmvc_checker
cp ./app.py \
	./njmvc_checker.py \
   	./njmvc_cron.txt \
	./requirements.txt \
	./entrypoint.sh \
	./init.sh \
	./local.env \
	./app

cp -r ./scraper \
	./email_client \
	./utils \
	./app/njmvc_checker

# Remove pycache
rm -r ./app/njmvc_checker/*/*cache*
rm -r ./app/njmvc_checker/*/.*cache*

# Zip folder
sudo zip -r ./njmvc_app.zip ./app
echo "Completed zipping application as njmvc_app.zip"

