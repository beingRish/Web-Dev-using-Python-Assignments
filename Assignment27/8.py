# 8. Write a python script to implement try except and else block for division.

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

except Exception:
    print("Kuchh to gadbad hai")
else:
    print("Sab Sahi hai ji")
