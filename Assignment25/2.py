"""
2. Write a python script to update the above Profile class with encapsulation.
"""


# creating Profile class
class Profile:
    def __init__(self):
        self.name = "Rishabh"
        self.email = 'rishabhjuly11@gmail.com'
        self.age = 24

    def display(self):
        print("Name=", self.name)
        print("Email=", self.email)
        print("Age=", self.age)


# creating an object
p = Profile()

# calling the display() method
p.display()
