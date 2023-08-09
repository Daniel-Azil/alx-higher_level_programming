#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        variable = number % 10
        print("{:d}".format(variable), end='')
        return (variable)
    else:
        variable = number % -10
        variable *= -1
        print("{:d}".format(variable), end='')
        return (variable)
