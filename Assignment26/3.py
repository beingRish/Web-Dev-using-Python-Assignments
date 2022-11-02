"""
3. Write a python script to create a to print the above user account object using operator
overloading (hint __str__ method).
"""


# creating a user account class
class UserAccount:
    def __init__(self, Uid, bal):
        self.Uid = Uid
        self.bal = bal

    def __str__(self):
        return str(self.Uid) + ":" + str(self.bal)

    def __add__(self, other):
        total_Uid = self.Uid + other.Uid
        total_bal = self.bal + other.bal
        return UserAccount(total_Uid, total_bal)


U1 = UserAccount(101, 50000)
U2 = UserAccount(102, 25000)
U3 = UserAccount(103, 75000)

print(U1 + U2 + U3)
