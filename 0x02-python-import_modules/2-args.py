#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    nargs = len(sys.argv) - 1

    if nargs == 0:
        print("{} arguments.".format(nargs))
    elif nargs == 1:
        print("{} argument:".format(nargs))
    else:
        print("{} arguments:".format(nargs))

    if nargs >= 1:
        j = 0
        for i in args:
            if j != 0:
                print("{}: {}". format(j, i))
            j += 1
