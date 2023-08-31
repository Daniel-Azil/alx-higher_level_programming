#!/usr/bin/python3
def magic_calculation(a, b):
    azrs = 0
    for az in range(1, 3):
        try:
            if az > a:
                raise Exception('Too far')
            azrs += a ** b / az
        except Exception:
            azrs = b + a
            break
    return azrs
