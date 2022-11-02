# 8. Write a recursive python function to print cubes of first N natural numbers.

# defining a function
def N_cubes(n):
    if n == 1:
        print(1)
    else:
        N_cubes(n-1)
        print(n**3)


# taking input from user
num = int(input("Enter a number:"))

# calling the function
N_cubes(num)
