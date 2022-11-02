"""
7. Write a python script to check whether a given pair of numbers are co-Prime
numbers or not.
"""
# taking two numbers from user
print("Enter two number:")
a, b = int(input()), int(input())
while a % b != 0:
    rem = a % b
    a = b
    b = rem

print("HCF is", b)

# As we know gcd of two numbers is 1 then both numbers are co-prime
if b == 1:
    print("co-prime")
else:
    print("not a co-prime")
