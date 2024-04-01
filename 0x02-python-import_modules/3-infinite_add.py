#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv_len = len(sys.argv)
    sum = 0

    if (argv_len == 1):
        print(sum)
    else:
        i = 1
        while i < argv_len:
            sum += int(sys.argv[i])
            i += 1
        print(sum)
