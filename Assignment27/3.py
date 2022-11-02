# 3. Write a python script to handle the ArithmeticError

a = 33
b = 0
c = 1
try:
    c = a/b
except ArithmeticError:
    print("You have just made a Arithmetic error.")

print(c)

