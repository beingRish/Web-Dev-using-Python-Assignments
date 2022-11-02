"""
1. Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements
"""


# defining a function
def unique_elements(l):
    # converting the list into set because set does not support duplicate value
    s = set(l)
    # returning the list value
    return list(s)


# list which is to be pass through the function calling
l1 = [34, 56, 76, 34, 78, 97, 56, 32, 56, 90]

# calling the function
print("List with unique elements is", unique_elements(l1))
