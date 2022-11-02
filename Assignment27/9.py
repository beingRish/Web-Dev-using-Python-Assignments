# 9. Write a python script to raise a ValueError.

from math import sqrt
try:
    a = int(input("Enter a number:"))

    if a < 0:
        raise ValueError()

    print(sqrt(a))

except ValueError:
    print("Negative Number ka square ni niklta pagal insan!")

