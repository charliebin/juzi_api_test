#!/bin/bash
#source lib/test.config

if [ $# -gt 1 ] 
then
    echo "Usage: "
    echo "sh run.sh <version>"
    echo "current supported version: > 2.1"
    exit 1
elif [ $# -eq 1 ]
then
    version=$1
elif [ $# -eq 0 ]
then
    version=`grep current_ver lib/test.config | awk -F'current_ver=v' '{print $2}'`
fi

cd basic_cases

cp v$version/* .

py.test test*

cd -
