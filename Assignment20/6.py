"""
6. Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30.
"""


# defining a function
def Square():
    l1 = []
    for i in range(1, 31):
        l1.append(i * i)
    print(l1)


# calling the function
Square()
