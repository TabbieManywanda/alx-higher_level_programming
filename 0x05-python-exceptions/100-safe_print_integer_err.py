#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        if isinstance(value, int) is True:
            print("{:d}".format(value))
            return True
        else:
            return False
    except (ValueError, TypeError) as err:
        print()
        sys.stderr.write("Exception: ", err)
        return False
