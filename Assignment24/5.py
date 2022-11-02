# 5. Write a python program to delete the age property of the user.

# creating a class
class User:
    name = "Rishabh"
    roll = 21
    age = 24

    def __init__(self):
        print("Name=", self.name)
        print("Roll=", self.roll)
        del self.age
        print("Age=", self.age)


# creating an object
obj = User()

