#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    if abs(number) % 10 == 0:
        last_number_var1 = (number) % 10
        print("Last digit of {:d} is {:d} and is 0".format(number, last_number_var1))
    elif abs(number) % 10 > 5:
        last_number_var2 = (number) % 10
        print("Last digit of {:d} is {:d} and is greater "
              "than 5".format(number, last_number_var2))
    elif abs(number) % 10 < 6:
        last_number_var3 = (number) % 10
        print("Last digit of {:d} is {:d} and is less than 6 "
        "and not 0".format(number, last_number_var3))
if number < 0:
    if number % -10 == 0:
        last_number_var4 = number % -10
        print("Last digit of {:d} is {:d} and is 0".format(number, last_number_var4))
    elif number % -10 < 0:
        last_number_var5 = number % -10
        print("Last digit of {:d} is {:d} and is less than "
              "6 and not 0".format(number, last_number_var5))
