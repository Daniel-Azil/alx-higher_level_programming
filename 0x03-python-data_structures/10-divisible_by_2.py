#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    stack_rnt = []
    for element in range(len(my_list)):
        if my_list[element] % 2 == 0:
            stack_rnt.append(True)
        else:
            stack_rnt.append(False)
    return (stack_rnt)
