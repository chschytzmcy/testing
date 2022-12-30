#!/bin/bash
# author:chenyan

cd docker/

docker build -t="registry.cn-hangzhou.aliyuncs.com/etsme/zz-pytest:$1" .
docker images | grep zz-pytest
docker push registry.cn-hangzhou.aliyuncs.com/etsme/zz-pytest:$1

