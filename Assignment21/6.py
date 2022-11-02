"""
6. Write a recursive python function to print first N even natural numbers in reverse
order.
"""


# defining a function
def N_Even_Reverse(n):
    # number should be more than zero
    if n >= 1:
        print(2 * n)
        # calling the recursive function
        N_Even_Reverse(n - 1)


# taking input from user
num = int(input("Enter a number:"))

# calling the function
N_Even_Reverse(num)
