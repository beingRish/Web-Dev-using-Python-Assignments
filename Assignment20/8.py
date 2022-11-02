"""
8. Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.
"""


# defining a function
def UC_LC():
    c1, c2 = 0, 0
    s = input("Enter a string:")
    for e in range(len(s)):
        if s[e].isupper():
            c1 += 1
        elif s[e].islower():
            c2 += 1
    print("Number of Upper Case Letters=", c1)
    print("Number of Lower Case Letters=", c2)


# calling the function
UC_LC()
