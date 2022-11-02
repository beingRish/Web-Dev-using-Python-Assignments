"""
6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
and division of 2 values and inherit it from the Calculator class.
"""


# creating a Calculator class
class Calculator:
    x = int(input("Enter value1:"))
    y = int(input("Enter value2:"))

    def adding(self):
        print("Addition=", self.x + self.y)

    def subtracting(self):
        print("Subtraction=", self.x - self.y)


class Calculator2(Calculator):
    def multiplication(self):
        print("Multiplication=", self.x * self.y)

    def division(self):
        print("Division=", self.x / self.y)


c = Calculator2()

c.adding()
c.subtracting()
c.multiplication()
c.division()
