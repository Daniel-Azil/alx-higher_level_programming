#!/usr/bin/python3
for small_letters in range(97, 123):
    if small_letters != 101 and small_letters != 113:
        print("{:c}".format(small_letters), end='')
