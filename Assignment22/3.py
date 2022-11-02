# 3. Write a recursive python function to calculate sum of first N even natural numbers

# defining a function
def sumEven(n):
    if n == 0:
        return 0
    else:
        s = (2*n) + sumEven(n-1)
    return s


# taking input from user
num = int(input("Enter a number:"))

# calling the function
print("Sum of first", num, "Even natural numbers=", sumEven(num))
