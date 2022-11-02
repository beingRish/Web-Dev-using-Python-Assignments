"""
3. Write a python program to create 2 objects of the user class and assign different
values.
"""


# creating a class
class User:
    # class variable
    Name = None
    Roll = None


# creating two objects
obj1 = User()
obj2 = User()

# Assigning the value of class variables through first object
obj1.Name = "Rishabh"
obj1.Roll = 21

# printing the value of class variables through first object
print(obj1.Name)
print(obj1.Roll)

# Assigning the value of class variables through second object
obj2.Name = "Shivam"
obj2.Roll = 2

# printing the value of class variables through first object
print(obj2.Name)
print(obj2.Roll)
