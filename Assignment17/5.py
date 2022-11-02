'''
5. Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
another_set= {"C", "Cpp", "Django"}
'''
this_set = {"Java", "Python", "SQL"}
another_set = {"C", "C++", "Django"}
l1 = list(another_set)
this_set.update(l1)
print(this_set)
