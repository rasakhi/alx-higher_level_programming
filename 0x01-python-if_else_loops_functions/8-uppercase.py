#!/usr/bin/python3
def uppercase(str):
    ustr = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            ustr = ustr + chr(ord(i) - 32)
        else:
            ustr = ustr + i
    print("{}".format(ustr))
