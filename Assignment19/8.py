# 8. Write a python program to multiply all the numbers in a list.

# defining a function
def mul_list(n):
    s = 1
    for e in range(len(n)):
        s = s * n[e]
    return s


l1 = [3, 64, 3, 7]
# calling the function with list arguments
print('Multiply=', mul_list(l1))
