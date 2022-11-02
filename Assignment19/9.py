'''
9. Write a python program to create a function to check whether a number falls in a
given range.
'''


# defining a function
def falls_or_not():
    s = (34, 54, 37, 42, 64, 67)
    n = int(input("Enter a number:"))
    if n in s:
        return True
    else:
        return False


print("The number falls") if falls_or_not() is True else print("The number does not falls.")
