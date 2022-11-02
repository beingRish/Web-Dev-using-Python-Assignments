# 5. Write a python script to calculate sum of first N even natural numbers
n = int(input("Enter a number:"))
i = 1
s = 0
for i in range(1, n + 1):
    s = s + 2 * i
print("Sum=", s)
