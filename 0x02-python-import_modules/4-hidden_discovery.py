#!/usr/bin/python3
import hidden_4

for i in dir(hidden_4):
    if i.startswith('__'):
        pass
    else:
        print("{}".format(i))
