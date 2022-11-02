# 1. Write a recursive python function to calculate sum of first N natural numbers

# defining a function
def sumN(n):
    if n == 1:
        return 1
    else:
        s = n + sumN(n-1)
    return s


# taking input from user
num = int(input("Enter a number:"))

# calling the function
print("Sum of first", num, "natural numbers=", sumN(num))

