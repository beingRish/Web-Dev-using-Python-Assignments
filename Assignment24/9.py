"""
9. Write a python program to create a School class and 3 instance variables and 1 class variable.
"""


# creating a School class
class School:
    # class variables
    Board = "CBSE"

    # defining a instance method to get value of instance variable from user
    def getInput(self):
        School.name = input("Enter School Name:")
        School.location = input("Enter School Location:")
        School.shortName = input("Enter School Short Name:")

    # defining a instance method to display value of instance variable
    def show(self):
        print("School Name =", self.name)
        print("School Location =", self.location)
        print("School Short Name =", self.shortName)


# creating an object
s = School()

# calling the getInput function
s.getInput()

# printing the class variable
print("Board of School =", s.Board)

# calling the show() method
s.show()
