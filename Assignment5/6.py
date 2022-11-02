'''
6. Write a python script which takes a three digits number from the user and displays
only its middle digit.
'''

# taking input from user
n = int(input("Enter three digit number: "))

# operation
n = n // 10
m = n % 10

# Output
print("Middle digit is", m)
