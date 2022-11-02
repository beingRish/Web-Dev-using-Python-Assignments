"""
1. Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in
a class using method overloading.
"""

# creating a class
class MethodOverloading:
    # defining a method
    def multiply(self, a, b=None, c=None, d=None):
        if d != None:
            s = a * b * c * d
        elif c != None:
            s = a * b * c
        else:
            s = a * b
        return s


m = MethodOverloading()
print("Multiply=", m.multiply(35, 89))
print("Multiply=", m.multiply(35, 89, 43))
print("Multiply=", m.multiply(32, 64, 32, 65))


