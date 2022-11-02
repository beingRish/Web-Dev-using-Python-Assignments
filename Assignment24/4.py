# 4. Write a python program to init default values for user object using __init__ method.

# creating a class
class User:
    name = None      # class variable
    roll = None

    def __init__(self):
        self.name = "Rishabh"         # instance variable
        self.roll = 21
        print("Name=", self.name)
        print("Roll=", self.roll)


# creating an object
obj = User()
