#!/bin/bash
set -x

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
    [[ $1 =~ ^.{6,12}$ ]] || return 1
}
check() {
    if [ "$1" == '' ];then
        return 0
    elif [[ "$1" = ,* ]];then
        check "$(echo "$1" | sed 's/^,//g')"
    else
        password="$(echo "$1" | cut -d, -f1)"
        check_pass $password
        if [ $? -eq 0 ];then
            if [ "$res" == '' ];then
                res="$password"
            else
                res="$res, $password"
            fi
        fi
        check "$(echo "$1" | sed "s/$password//g")"
    fi
}
check_pass() {
    check_digits "$1" && \
    check_high "$1" && \
    check_low "$1" && \
    check_special "$1" && \
    check_len "$1"
}

main() {
    res=''
    check "$(cat data/passwords.txt)"
    echo "$res"
}

main
