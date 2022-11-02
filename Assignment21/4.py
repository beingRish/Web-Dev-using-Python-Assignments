# 4. Write a recursive python function to print first N odd natural numbers in reverse order

# defining a function
def N_Odd_Reverse(n):
    if n == 1:
        print(1)
    else:
        print((2 * n) - 1)
        N_Odd_Reverse(n-1)


# taking input from user
num = int(input("Enter a number:"))

# calling the function
N_Odd_Reverse(num)
