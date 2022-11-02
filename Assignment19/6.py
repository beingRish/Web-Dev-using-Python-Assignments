# 6. Write a python program to create a function that finds a maximum of four numbers.

# defining a function
def max_num(a, b, c, d):
    if a > b and a > c:
        return a
    elif b > c and b > d:
        return b
    elif c > d:
        return c
    else:
        return d


print("Enter four numbers:")
n1, n2, n3, n4 = int(input()), int(input()), int(input()), int(input())
# calling a function
print("Maximum Number is", max_num(n1, n2, n3, n4))
