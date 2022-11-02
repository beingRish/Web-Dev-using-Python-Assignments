# 7. Write a python script to print first N even natural numbers in reverse order
n = int(input("Enter a number:"))
for i in range(n, 0, -1):
    print(2 * i, end=' ')
