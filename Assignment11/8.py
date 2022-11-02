# 8. Write a python script to calculate sum of digits of a given number
"""n =int(input("Enter a number:"))
s = 0
r = 0
while n > 0:
    r = n % 10
    s = s + r
    n = n // 10
print("Sum=", s)
"""
n = input("Enter a number:")
print(sum([int(e) for e in n]))
