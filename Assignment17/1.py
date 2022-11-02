# 1. Write a python program to store all the programming languages known to you using set.

# taking input from user
l = input("Enter languages separated by comma: ")

# storing the data in variable by splitting by comma.
language = {eval(e) for e in l.split(',')}

# printing the data
print(language)
