# 6. Write a python program to create 3 user objects and find the youngest of all.

# creating a class
class User:
    a = None


obj1 = User()
obj1.a = 45
obj2 = User()
obj2.a = 67
obj3 = User()
obj3.a = 32

if obj1.a > obj2.a and obj3.a:
    print(obj1.a, "is youngest.")
elif obj2.a > obj3.a:
    print(obj2.a, "is youngest.")
else:
    print(obj3.a, "is youngest.")
