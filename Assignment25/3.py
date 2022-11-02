"""
3. Write a python script to update 2nd Question, change email and age to __email and
__age.
"""


# creating Profile class
class Profile:

    def __init__(self):
        self.name = "Rishabh"
        self.__email = 'rishabhjuly11@gmail.com'
        self.__age = 24

    def display(self):
        print("Name=", self.name)
        print("Email=", self.__email)
        print("Age=", self.__age)


# creating an object
p = Profile()

# calling the display() method
p.display()
