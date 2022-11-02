'''
5. Write a python script which takes a three digit number from the user and displays
only its first digit.
'''

# taking input as number from user
n = int(input("Enter three digit number: "))

# operation
first_digit = n//100
print("First digit is", first_digit)