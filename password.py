#!/usr/bin/python2.7

import sys
import random


class Password:

    def __init__(self, length):
        self.wordlist = self.get_wordlist()
        self.password = []
        self.generate_password(length)

    def get_wordlist(iself, file='/usr/share/dict/american-english'):
        with open(file, 'r') as wordlist:
            return wordlist.read().splitlines()

    def random_index(self):
        return random.randint(0, len(self.wordlist) - 1)

    def generate_password(self, password_length):
        for number in range(password_length):
            self.password.append(self.wordlist[self.random_index()].replace("'", ""))

    def short(self):
        return ''.join(self.password)

    def long(self):
        return self.password


class Banner:

    @staticmethod
    def display(password_string, password_array):
        print ''
        print " Graham's password generating script v1.3.1 "
        print ''
        print ' Your password:    ' + password_string
        print ''
        print ' =========================='
        print ''
        print 'Easier to remember as:'
        for element in password_array:
            print ' ' + element
        print ''

    @staticmethod
    def usage():
        print ''
        print " Graham's password generating script v1.3.1 "
        print ''
        print ' Usage: password.py <password length 3-10> [--quiet]'
        print ' Sadly we only support a password length between 3 and 10 words\n'
        print ''


__all__ = ['Password']

if __name__ == '__main__':

    if len(sys.argv) == 3 and int(sys.argv[1]) > 2 and int(sys.argv[1]) < 11 and sys.argv[2] == '--quiet':

        print Password(int(sys.argv[1])).short()

    elif len(sys.argv) == 2 and int(sys.argv[1]) > 2 and int(sys.argv[1]) < 11:

        password = Password(int(sys.argv[1]))
        Banner.display(password.short(), password.long())

    else:

        Banner.usage()
