"""6. Write a python program to append elements from another list to the current list.
(firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )
"""
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
for i in range(len(firstlist)):
  secondlist.append(firstlist[i])
print(secondlist)
