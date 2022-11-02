"""
10. Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values
"""


# creating a class Employee
class Employee:
    def __init__(self):
        self.salary = None
        self.name = None
        self.emp_id = None

    def getInput(self):
        self.emp_id = input("Enter Employee ID:")
        self.name = input("Enter Employee Name:")
        self.salary = input("Enter Employee Salary:")

    def display(self):
        print("Employee ID =", self.emp_id)
        print("Employee Name =", self.name)
        print("Employee Salary =", self.salary)


e = Employee()
e.getInput()
e.display()
