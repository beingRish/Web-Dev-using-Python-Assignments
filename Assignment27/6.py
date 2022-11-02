"""
6. Write a python script to create a calculator with 4 basic operations, and handle a
maximum number of exceptions.
"""

try:
    a, b = int(input("Enter first number:")), int(input("Enter second number:"))

    add = a + b
    sub = a - b
    mul = a * b
    div = a / b

    print("Addition=", add)
    print("Subtraction=", sub)
    print("Multiplication=", mul)
    print("Division=", div)

except ZeroDivisionError:
    print("Zero Se Divide mat kiya kro yaar")

except ValueError:
    print("Are kewal integer Enter kro na Yaar")


