# 6. Write a python script to calculate factorial of a given number
n = int(input("Enter a number:"))
f = 1
for i in range(1, n + 1):
    f = f * i
print("Factorial=", f)
