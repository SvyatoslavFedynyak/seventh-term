#!/bin/bash
set -x
passwords=`cat data/passwords.txt`
res=""
echo "$passwords"
input=`echo "$passwords" | tr ',' '\n'`
while IFS= read -r password
do
    len=`echo "$password" | wc -m`
    if [ "$len" -le 6 ] || [ "$len" -ge 12 ];then
        continue
    fi
    echo "$password" | grep -q '[a-z]'
    if [ $? -ne 0 ];then
        continue
    fi
    echo "$password" | grep -q '[A-Z]'
    if [ $? -ne 0 ];then
        continue
    fi
    echo "$password" | grep -q '[0-9]'
    if [ $? -ne 0 ];then
        continue
    fi
    echo "$password" | grep -q '[$#@]'
    if [ $? -ne 0 ];then
        continue
    fi
    if [ "$res" == "" ];then
            res="$password"
        else
            res="$res, $password"
    fi
done <<< "$input"
echo "$res"