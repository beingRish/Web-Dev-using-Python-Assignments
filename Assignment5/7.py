'''
7. Write a python script which takes a three digits number from the user and displays
only its last digit.
'''

# taking input from user
n = int(input('Enter three digit number: '))

# Operation
l = n % 10

# Output
print("First digit is", l)
