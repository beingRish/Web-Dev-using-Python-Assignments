# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers

# defining a function
def sumCubes(n):
    if n == 1:
        return 1
    else:
        s = (n**3) + sumCubes(n - 1)
    return s


# taking input from user
num = int(input("Enter a number:"))

# calling the function
print("Sum of cubes of", num, "natural numbers=", sumCubes(num))


