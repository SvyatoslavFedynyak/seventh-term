import re

passwords = open('data/passwords.txt', 'r').readline().split(',')
print('Source: {}'.format(passwords))
res = []
for password in passwords:
    if len(password) < 6 or len (password) > 12:
        continue
    if not re.search('[a-z]', password):
        continue
    if not re.search("[0-9]", password):
        continue
    if not re.search("[A-Z]", password):
        continue
    if not re.search("[$#@]", password):
        continue
    res.append(password)
print (res)

