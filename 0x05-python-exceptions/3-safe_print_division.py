#!/usr/bin/python3

def safe_print_division(a, b):
    """Implementation of try and execept funtionality."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
