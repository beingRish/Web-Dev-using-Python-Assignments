# 8. Write a python script to check if a string contains only numbers.
s = input("Enter a String:")
if s.isnumeric():
    print("String contains only numbers.")
else:
    print("String does not contain only numbers.")