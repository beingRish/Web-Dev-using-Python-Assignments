"""
9. Write a python script to create an application like Truecaller where names and
numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
number and 2nd to add a new entry).
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


t = Truecaller()
t.addNewEntry()
t.fetchName()
