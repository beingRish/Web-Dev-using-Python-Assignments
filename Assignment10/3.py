# 3. Write a python script to print first N natural numbers in reverse order
n = int(input("Enter a number:"))
for n in range(n, 0, -1):
    print(n, end=' ')
