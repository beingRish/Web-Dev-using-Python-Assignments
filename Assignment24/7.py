"""
7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
values).
"""


# creating a Laptop class
class Laptop:
    # 4 attributes
    brand = None
    ram = None
    cpu = None
    hdd = None

    # --init--() method
    def __init__(self):
        # initializing the values to the attributes
        self.brand = input("Enter Brand Name:")
        self.ram = input("Enter RAM:")
        self.cpu = input("Enter CPU:")
        self.hdd = input("Enter Hard disk:")

    # defining showConfig() method to print the values
    def showConfig(self):
        print("Brand=", self.brand, "\nRAM=", self.ram, "\nCPU=", self.cpu, "\nHard disk=", self.hdd)


# creating an object
l = Laptop()

# calling the showConfig() method through the object
l.showConfig()
