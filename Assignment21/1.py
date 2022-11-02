# 1. Write a recursive python function to print first N natural numbers.

# defining a function
def N_natural(n):
    # the number should be greater than zero
    if n > 0:
        # calling the recursive function
        N_natural(n - 1)
        print(n)


# taking input from user
num = int(input("Enter a number:"))

# calling the function
N_natural(num)
