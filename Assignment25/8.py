"""
8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
Phone Class.
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


class Phone:
    @staticmethod
    def calling():
        print("You can Call after dialing the number.")

    @staticmethod
    def sms():
        print("You can text after typing something.")


class SmartPhone(Calculator2, Phone):
    @staticmethod
    def whatsApp():
        print("You Can Call, text someone via WhatsApp")

    @staticmethod
    def facebook():
        print("You can use facebook")

    @staticmethod
    def YouTube():
        print("You can watch video on YouTube")


s = SmartPhone()
s.whatsApp()
s.facebook()
s.YouTube()
s.adding()
s.subtracting()
s.multiplication()
s.division()
s.calling()
s.sms()
