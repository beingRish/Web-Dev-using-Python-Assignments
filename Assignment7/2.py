f'''
2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division
'''
print("Press 1 to Addition.")
print("Press 2 to Subtraction.")
print("Press 3 to Multiplication.")
print("Press 4 to Division.")
c = int(input("Enter what operation you want to do: "))
match c:
    case 1:
        print("Enter two numbers:")
        x, y = int(input()), int(input())
        print("Addition=", x + y)
    case 2:
        print("Enter two numbers:")
        x, y = int(input()), int(input())
        print("Subtraction=", x - y)
    case 3:
        print("Enter two numbers:")
        x, y = int(input()), int(input())
        print("Multiplication=", x * y)
    case 4:
        print("Enter two numbers:")
        x, y = int(input()), int(input())
        print("Division=", x / y)
    case other:
        print("invalid operation")
