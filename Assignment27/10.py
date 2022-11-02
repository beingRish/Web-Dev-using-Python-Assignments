# 10. Write a python script to implemented a nested Try Except block

try:
    print("Outer try block")
    print(10/3)
    try:
        print("Inner try block")
    except ZeroDivisionError:
        print("Inner except block")
except:
    print("Outer except block")
