# 4. Write a python script to calculate sum of first N odd natural numbers
n = int(input("Enter a number:"))
s = 0
for i in range(1, n + 1):
    s = s + (2 * i - 1)
print("Sum=", s)
