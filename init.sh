#!/usr/bin/bash
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y wget
apt-get install -y zip unzip
unzip njmvc_checker.zip &&
rm njmvc_checker.zip
mv njmvc_checker/* .
rmdir njmvc_checker

#apt-get install -y python3.9
apt-get install -y python3-pip
pip install -r requirements.txt

# todo: add chromedriver, Chrome browser
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get install -y ./google-chrome-stable_current_amd64.deb

wget https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin
rm chromedriver_linux64.zip

source local.env
