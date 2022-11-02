"""10. Write a Python script to create a list, where each element of the list is a
digit of a given number.
"""
n = int(input("Enter a number:"))
n1 = str(n)
list1 = []
for i in range(len(n1)):
    list1.insert(i, n1[i])
print(list1)
