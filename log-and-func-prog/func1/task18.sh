#!/bin/bash
check_digits() {
    echo "$1" | grep -q '[0-9]'
    return $?
}
check_low() {
    echo "$1" | grep -q '[a-z]'
    return $?
}
check_high() {
    echo "$1" | grep -q '[A-Z]'
    return $?
}
check_special() {
    echo "$1" | grep -q '[#$@]'
    return $?
}
check_len() {
    len=`echo "$1" | wc -m`
    if [ $len -le 6 ] || [ $len -ge 12 ];then
        return 1
    fi
}
check() {
    curr_string=$1
    if [ "$curr_string" == '' ];then
        return 0
    elif [[ "$curr_string" = ,* ]];then
        curr_string=`echo "$curr_string" | sed 's/^,//g'`
        check "$curr_string"
    else
        password=`echo "$curr_string" | cut -d, -f1`
        check_digits "$password" && \
        check_high "$password" && \
        check_low "$password" && \
        check_special "$password" && \
        check_len "$password"
        if [ $? -eq 0 ];then
            if [ "$res" == '' ];then
                res="$password"
            else
                res="$res, $password"
            fi
        fi
        curr_string=`echo "$curr_string" | sed "s/$password//g"`
        check "$curr_string"
    fi
}

main() {
    passwords=`cat data/passwords.txt`
    res=''
    check "$passwords"
    echo "$res"
}

main
