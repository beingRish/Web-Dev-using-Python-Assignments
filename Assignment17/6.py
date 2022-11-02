'''6. Write a python program to add elements of list to a set
this_set = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
'''
this_set = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
this_set.update(mylist)
print(this_set)
