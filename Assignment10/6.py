# 6. Write a python script to print first N even natural numbers
n = int(input("Enter a number:"))
for i in range(1, n + 1):
    print(2 * i, end=' ')
