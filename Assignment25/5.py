"""
5. Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values.
"""


# creating a Calculator class
class Calculator:
    x = int(input("Enter value1:"))
    y = int(input("Enter value2:"))

    def adding(self):
        print("Addition=", self.x + self.y)

    def subtracting(self):
        print("Subtraction=", self.x - self.y)


c = Calculator()

c.adding()
c.subtracting()

