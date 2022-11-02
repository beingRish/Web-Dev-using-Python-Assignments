# 5. Write a python program to create a function to find the Min of three numbers.

# defining a function
def min_number(a, b, c):
    if a < b and a < c:
        return a
    elif b < c:
        return b
    else:
        return c


# taking input from user
print("Enter three numbers:")
x, y, z = int(input()), int(input()), int(input())

# printing the minimum number via function call
print("Minimum number is", min_number(x, y, z))
