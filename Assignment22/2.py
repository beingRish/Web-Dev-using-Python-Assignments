# 2. Write a recursive python function to calculate sum of first N odd natural numbers

# defining a function
def sumOdd(n):
    if n == 1:
        return 1
    else:
        s = (2*n-1) + sumOdd(n-1)
    return s


# taking input from user
num = int(input("Enter a number:"))

# calling the function
print("Sum of first", num, "Odd natural numbers=", sumOdd(num))
