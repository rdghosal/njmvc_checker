#!/usr/bin/bash
export DEBIAN_FRONTEND=noninteractive
apt-get update
echo "========== Installing wget and zip/unzip =========="
apt-get install -y wget
apt-get install -y zip unzip

echo "========== Installing cron =========="
apt-get install -y cron

# Assumes that python is pre-installed in environment.
# Otherwise, uncomment the below line.
#apt-get install -y python3.9

echo "========== Installing pip =========="
apt-get install -y python3-pip
pip install -r requirements.txt

# Chrome Browser/Driver are v90
echo "========== Installing Google Chrome =========="
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y ./google-chrome-stable_current_amd64.deb

echo "========== Installing chromedriver ==========" 
wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin
rm chromedriver_linux64.zip

echo "========== Preparing current directory ==========" 
chmod +x ./entrypoint.sh

unzip njmvc_checker.zip &&
rm njmvc_checker.zip
mv njmvc_checker/* .
rmdir njmvc_checker