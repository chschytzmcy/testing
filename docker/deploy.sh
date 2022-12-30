#!/bin/bash

# install jdk8
apt-get install -y openjdk-8-jdk

# install allure
tar -zxvf /root/allure-commandline-2.18.0.tgz -C /root/
ln -s /root/allure-2.18.0/bin/allure /bin/allure

# mkdir test dir
mkdir /root/test

