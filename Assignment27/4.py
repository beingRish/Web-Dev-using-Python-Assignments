# 4. Write a python script to handle a ValueError

from math import sqrt

a = -4
s = 0
try:
    s = sqrt(a)
except ValueError:
    print("You can not get square root of a negative number.")

print(s)


