#!/bin/bash
check_digits() {
    password=$1
    echo "$password" | grep -q '[0-9]'
    return $?
}
check_low() {
    password=$1
    echo "$password" | grep -q '[a-z]'
    return $?
}
check_high() {
    password=$1
    echo "$password" | grep -q '[A-Z]'
    return $?
}
check_special() {
    password=$1
    echo "$password" | grep -q '[#$@]'
    return $?
}
check_len() {
    password=$1
    len=`echo "$password" | wc -m`
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
