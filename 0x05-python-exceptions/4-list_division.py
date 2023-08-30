#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    azl = []
    for az in range(list_length):
        try:
            azrs = my_list_1[az] / my_list_2[az]
        except ZeroDivisionError:
            print("division by 0")
            azrs = 0
        except TypeError:
            print("wrong type")
            azrs = 0
        except IndexError:
            print("out of range")
            azrs = 0
        finally:
            azl.append(azrs)

    return (azl)
