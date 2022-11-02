'''
4. Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same.
'''
'''n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print(n1 or n2)
'''

print("Enter two numbers:")
a, b = int(input()), int(input())
print(a if a > b else b)
