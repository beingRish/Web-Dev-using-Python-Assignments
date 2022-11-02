"""
4. Write a python script to update 2nd Question, add a class variable (platform) and
create a class method to access it.
"""


class Profile:
    platform = input("Enter platform:")

    def __init__(self):
        self.name = "Rishabh"
        self.email = 'rishabhjuly11@gmail.com'
        self.age = 24

    def display(self):
        print("Name=", self.name)
        print("Email=", self.email)
        print("Age=", self.age)

    @classmethod
    def class_method(cls):
        print(cls.platform)


# creating an object
p = Profile()

# calling the display() method
p.display()
p.class_method()
