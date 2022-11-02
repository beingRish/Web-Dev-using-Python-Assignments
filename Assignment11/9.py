"""9. Write a python script to print binary equivalent of a given decimal number.
(do not use bin() method)"""
n = int(input("Enter a number: "))
b = ' '
while n != 0:
    r = n % 2
    b = b + str(r)
    n = n // 2
print("Binary is:")
for i in range(len(b) - 1, -1, -1):
    print(b[i], end=' ')
