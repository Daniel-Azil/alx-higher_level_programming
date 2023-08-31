#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        azrs = fct(*args)
    except Exception as az:
        sys.stderr.write("Exception: {}\n".format(az))
        azrs = None

    return (azrs)
