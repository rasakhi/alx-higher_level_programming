#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number < 0:
    ld = -ld
print(f"Last digit of {number} is {ld} and is ", end="")
if ld > 5:
    print("greater than 5")
elif ld > 0 and ld < 6:
    print("less than 6 and not 0")
else:
    print("0")
