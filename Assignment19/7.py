# 7. Write a python program to sum all the numbers in a list.

# defining a function
def sum_list():
    l1 = [54, 65, 76, 87, 43, 32, 76, 43, 232, 75, 13, 654, 23, 86, 124]
    s = 0
    for e in range(len(l1)):
        s = s + l1[e]
    return s

    
# calling the function
print("Sum of numbers in the list = ", sum_list())

