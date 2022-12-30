FROM ubuntu:20.04

RUN apt-get -y update
RUN apt-get install -y curl net-tools tcpdump iputils-ping sqlite vim
RUN apt-get install -y python3 pip

RUN pip install requests
RUN pip install xlrd==1.2.0
#RUN pip install xlrd

RUN pip install -U pytest
RUN pip install allure-pytest

#apt-get install -y openjdk-8-jdk

COPY allure-commandline-2.18.0.tgz /root/allure-commandline-2.18.0.tgz
COPY deploy.sh /root/deploy.sh
COPY run.sh /root/run.sh

ENTRYPOINT [ "/bin/bash", "/root/run.sh" ]
