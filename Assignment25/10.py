"""
10. Write a python script to add the new method in SmartPhone class which accepts
Truecaller object as a parameter and call the fetch method of Truecaller..
"""


class Truecaller:
    number = None
    name = None
    n = {}

    def addNewEntry(self):
        while True:
            ans = input("Do you want to add New Entry[y/n]:")
            if ans == 'y':
                self.number = int(input("Enter number:"))
                self.name = input("Enter Name:")
                Truecaller.n[self.number] = self.name
            else:
                break

    def fetchName(self):
        for e in Truecaller.n:
            print(e, Truecaller.n[e])


class SmartPhone(Truecaller):
    @staticmethod
    def whatsApp():
        print("You Can Call, text someone via WhatsApp")

    @staticmethod
    def facebook():
        print("You can use facebook")

    @staticmethod
    def YouTube():
        print("You can watch video on YouTube")

    def Contact(self, obj):
        print(obj.fetchName())


t = Truecaller()

s = SmartPhone()
s.addNewEntry()
s.Contact(t)


