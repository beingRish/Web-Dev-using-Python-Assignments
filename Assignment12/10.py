# 10. Write a python script to calculate HCF of two numbers.

# taking two numbers from user
print("Enter two number:")
a, b = int(input()), int(input())
r = range(a if a < b else b, 1, -1)
for i in r:
    if a % i == 0 and b % i == 0:
        break
print("HCF=", i)
