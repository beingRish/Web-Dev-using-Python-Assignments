# 5. Write a python program to create a function which expects a list as an argument.

# defining a function
def numbers(n):
    print(n)


n1 = int(input("Enter a number:"))
l1 = list(range(1, n1 + 1))
# calling the function with list arguments
numbers(l1)
