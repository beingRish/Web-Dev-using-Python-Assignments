# 5. Write a recursive python function to print first N even natural numbers.

# defining a function
def N_Even(n):
    # number should be more than zero
    if n >= 1:
        # calling the recursive function
        N_Even(n-1)
        print(2*n)


# taking input from user
num = int(input("Enter a number:"))

# calling the function
N_Even(num)

