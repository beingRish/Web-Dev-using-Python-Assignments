'''
7. Write a python program to copy elements 4 and 5 from the following tuple into a new
tuple. tuple1=(1,2,3,4,5,6)
'''

tuple1 = (1, 2, 3, 4, 5, 6)
l1 = list(tuple1)
l2 = []

for e in range(len(l1)):
    if l1[e] == 4:
        l2.insert(0, l1[e])
    elif l1[e] == 5:
        l2.insert(1, l1[e])
print(tuple(l2))
