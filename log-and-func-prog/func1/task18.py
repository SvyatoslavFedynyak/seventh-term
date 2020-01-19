import itertools
import string
from functools import reduce
import re
import os

def check(passwords, *functions):
    return reduce(lambda res, f: f(res), list(functions), passwords)

def read_data():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'passwords.txt'), 'r') as file:
        return [x for x in file.read().split(",")]
    
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
    return list(filter(lambda x: len(x)>=6 and len(x)<=12, passwords))
def lowercase_check(passwords):
    return list(filter (password_has_lowercase_letters, passwords))
def uppercase_check(passwords):
    return list(filter(lambda x: re.search("[A-Z]", x), passwords))
def digits_check(passwords):
    return list(filter(password_has_digits, passwords))

def special_symbol_check(func, symb):
    def inner(passwords):
        return func(passwords, symb)
    return inner

def symb_check(passwords, symbols=""):
    return list(filter(lambda x: (len(set(x).intersection(set(symbols))) != 0), passwords))

def main():
    print(check(read_data(), lowercase_check, uppercase_check, digits_check, length_check, special_symbol_check(symb_check, '$#@')))
main()