#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    for i in sys.argv:
        if i != sys.argv[0]:
            total += int(i)
    print(total)
