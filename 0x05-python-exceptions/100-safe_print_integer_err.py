#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        if isinstance(value, int) is True:
            print("{:d}".format(value))
            return True
        else:
            print()
            return False
    except ValueError as err:
        sys.stderr.write("Exception: ", err)
        return False
