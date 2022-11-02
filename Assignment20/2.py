"""
2. Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not.
"""


# defining a function
def PrimeOrNot(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1

    print("Prime") if c == 2 else print("Not Prime")


# Taking input from user
n1 = int(input("Enter a number:"))

# function calling
PrimeOrNot(n1)
