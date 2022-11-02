# 6. Write a python script to check whether a given number is a three digit number or not.
'''n = int(input("Enter a number: "))
if 99 < n < 1000:
    print("Three Digit number")
else:
    print("Not a three digit number")'''

print("Three Digit number" if 99 < int(input("Enterr a number:")) < 1000 else "Not a three digit number")