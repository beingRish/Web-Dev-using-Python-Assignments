# 7. Write a recursive python function to print squares of first N natural numbers

# defining a function
def N_square(n):
    if n == 1:
        print(1)
    else:
        N_square(n-1)
        print(n*n)


# taking input from user
num = int(input("Enter a number:"))

# calling the function
N_square(num)