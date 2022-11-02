'''
8. Write a python program to convert two lists into a dictionary in a way that item from
list1 is the key and item from list2 is the value.
'''
list1 = [18, 19, 20, 21, 22]
t1 = tuple(list1)
list2 = ['Bhanu', 'Suman', 'Ranjay', 'Rishabh', 'Khushboo']
t2 = tuple(list2)
d1 = {}

for e in range(len(t1)):
    d1[t1[e]] = t2[e]
print(d1)
