# 2. Write a python script to check whether a given number is divisible by 5 or not
'''
# taking input from user
n = int(input("Enter a number: "))

# checking condition
if n % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5")'''

print("The number is not divisible by 5." if int(input("Enter a number: ")) %5 else "The number is divisible by 5")