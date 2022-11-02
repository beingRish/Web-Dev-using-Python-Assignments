# 5. Write a python script to print first N odd natural numbers in reverse order
n = int(input("Enter a value:"))
i = n
while i >= 1:
    print(2 * i - 1, end=' ')
    i -= 1
