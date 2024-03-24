#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv_len = len(sys.argv)
    if (argv_len == 1):
        print(f"{argv_len - 1} arguments.")
    elif (argv_len > 2):
        print(f"{argv_len - 1} arguments:")
        i = 1
        while i < argv_len:
            print(f"{i}: {sys.argv[i]}")
            i += 1
    else:
        print(f"{argv_len - 1} argument:")
        i = 1
        print(f"{i}: {sys.argv[i]}")
