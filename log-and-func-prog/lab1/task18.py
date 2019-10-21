import itertools
import string
from functools import reduce
import re

def check(passwords, *functions):
    funcs = list(functions)
    result  = reduce(lambda res, f: f(res), funcs, passwords)
    return result

def read_data():
    all_passwords = open('data/passwords.txt', 'r').read()
    passwords = [x for x in all_passwords.split(",")]
    return passwords
    
def password_has_digits( current_string, index = 0):
    if(index == len(current_string)):
        return False

    if current_string[index] in (str(x) for x in range(0,10)):
        return True
    else:
        return password_has_digits(current_string, index+1)

def password_has_lowercase_letters(current_string, index = 0):
    if index == len(current_string):
        return False
    if current_string[index] in [x for x in string.ascii_lowercase]:
        return True
    else:
        return password_has_lowercase_letters(current_string, index+1)

def length_check(passwords):
    result = list(filter(lambda x: len(x)>=6 and len(x)<=12, passwords))
    return result
def lowercase_check(passwords):
    result = list(filter (password_has_lowercase_letters, passwords))
    return result
def uppercase_check(passwords):
    result = list(filter(lambda x: re.search("[A-Z]", x), passwords))
    return result
def digits_check(passwords):
    result = list(filter(password_has_digits, passwords))
    return result

def special_symbol_check(func, symb):
    def inner(passwords):
        result = func(passwords, symb)
        return result
    return inner


def symb_check(passwords, symbols=""):
    result = list(filter(lambda x: (len(set(x).intersection(set(symbols))) != 0), passwords))
    return result

def main():
    passwords = read_data()
    #valid password example: ABcd12@dnj, not valid - abc1
    inner_symbol_check = special_symbol_check(symb_check, '$#@')
    res = check(passwords, lowercase_check, uppercase_check, digits_check, length_check, inner_symbol_check)
    print(res)
main()