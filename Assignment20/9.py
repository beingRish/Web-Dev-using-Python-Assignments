"""
9. Write a python program to create a function to check whether a string is a pangram
or not.
"""


# defining a function
def check_pangram(s):
    # create a set with unique characters
    temp = set(s.lower()) - set(' ')

    if len(temp) == 26:
        print("pangram")
    else:
        print("not pangram")


s1 = input("Enter a string")
check_pangram(s1)
