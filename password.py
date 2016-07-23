#!/usr/bin/python2.7

import sys
import random

print " \n Graham's password generating script v1.2.1 \n "

if len(sys.argv) == 2:
    if int(sys.argv[1]) > 2 and int(sys.argv[1]) < 11:
        password_length = int(sys.argv[1])
    else:
        print ' Usage: password.py <password length 3-10>'
        print ' Sadly we only support a password length between 3 and 10 words\n'
        exit()
else:
    print ' Usage: password.py <password length 3-10>\n'
    exit()

file = open('/usr/share/dict/american-english' , 'r')
word_list = file.read().splitlines()

password = ''
password_list = []

for number in range(password_length):
    random_index = random.randint(0 , len(word_list) - 1)
    word = word_list[random_index].replace("'" , '')
    password += word
    password_list.append(word)

print 'Your password:    ' +  password + '\n'
print '=' * 20
print '\nEasier to remember as: \n'
for element in password_list:
    print ' ' + element
print ''
