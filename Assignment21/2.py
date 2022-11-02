# 2. Write a recursive python function to print first N natural numbers in reverse order.

# defining a function
def N_reverse(n):
    while n:
        print(n)
        N_reverse(n - 1)
        if 1:
            break


# taking input from user
num = int(input("Enter a number:"))

# calling the function
N_reverse(num)
