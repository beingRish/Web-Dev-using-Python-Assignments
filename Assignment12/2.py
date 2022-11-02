# 2. Write a python script to check whether a given number is Prime or not
n = int(input("Enter a number: "))
c = 0
for i in range(1, n + 1):
    if n % i == 0:
        c += 1
if c == 2:
    print("Prime Number")
else:
    print("Not Prime Number")
