'''
1. Write a python program to create and print a dictionary which stores your information.
(name, age, gender …..)
'''
n = int(input("Enter a number:"))
d = {}
for e in range(n):
    key = eval(input("Enter key:"))
    value = eval(input("Enter value:"))
    d[key] = value
print(d)


# d1 = {'name': 'Rishabh', 'age': 24, 'gender': 'male'}
# print(d1)
