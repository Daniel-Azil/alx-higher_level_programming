#!/usr/bin/python3
for reversed_alphabet in reversed(range(97, 123)):
    if reversed_alphabet % 2 == 0:
        print("{:c}".format(reversed_alphabet), end='')
    else:
        print("{:c}".format(reversed_alphabet - 32), end='')
