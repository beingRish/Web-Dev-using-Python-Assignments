"""
4. Write a python program to create a function that checks whether a passed string is
palindrome or not.
"""


# defining a function
def check_Palindrome(s):
    # assigning the string into another value
    s1 = s

    # reversing the string through slicing
    r = s[len(s)+1::-1]

    # printing palindrome if old string is equal to reversed string else printing Not palindrome
    print("Palindrome") if s1 == r else print("Not Palindrome")


# taking string as input from user
s = input("Enter a string:")

# function call
check_Palindrome(s)
