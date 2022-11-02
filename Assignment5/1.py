'''
1. Write a python script to remove the last digit from a given number. (for example, if
user enters 2534 then your output should be 253)
'''

# taking input from user
n = int(input("Enter a number:"))

# use case, number = 2534, output = 253
# operation, number//10
r = n//10

# output
print("The number is", n)
print("After Removing last digit the number is", r)