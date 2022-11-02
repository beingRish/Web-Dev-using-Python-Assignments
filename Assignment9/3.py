# 3. Write a python script to print first N natural numbers in reverse order
n = int(input("Enter a value:"))
i = n
while i >= 1:
    print(i, end=' ')
    i -= 1
