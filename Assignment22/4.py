"""
4. Write a recursive python function to calculate sum of squares of first N natural
numbers.
"""


# defining a function
def sumSquare(n):
    if n == 1:
        return 1
    else:
        s = (n * n) + sumSquare(n - 1)
    return s


# taking input from user
num = int(input("Enter a number:"))

# calling the function
print("Sum of squares of", num, "natural numbers=", sumSquare(num))
