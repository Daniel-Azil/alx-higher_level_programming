#!/usr/bin/python3
def uppercase(str):
    for alphabet_character in range(len(str)):
        if ord(str[alphabet_character]) >= 97 and \
           ord(str[alphabet_character]) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[alphabet_character]) - num), end='')
    print()
