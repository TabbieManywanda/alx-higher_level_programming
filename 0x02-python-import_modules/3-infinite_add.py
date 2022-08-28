#!usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv)

    total = 0
    for i in range(nargs):
        total += int(sys.argv[i])
    print(total)
