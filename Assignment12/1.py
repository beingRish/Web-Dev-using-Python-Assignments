# 1. Write a python script to reverse a number.
n = int(input("Enter a number: "))
s = 0
while n > 0:
    r = n % 10
    s = s*10 + r
    n = n // 10
print("Reverse is", s)
