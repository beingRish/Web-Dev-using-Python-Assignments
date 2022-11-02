# 3. Write a recursive python function to print first N odd natural numbers

# defining a function
def N_Odd(n):
    if n == 1:
        print(1)
    else:
        N_Odd(n-1)
        print((2*n)-1)


# taking input from user
num = int(input("Enter a number:"))

# calling the function
N_Odd(num)
