#!/usr/bin/python3
for i,j in zip(range(122, 96, -2), range(89, 64, -2)):
    print("{:c}{:c}".format(i, j), end="")
