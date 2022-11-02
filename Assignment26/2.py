"""
2. Write a python script to create a user account class with 2 instance variables (userid
and balance). Create 3 user objects and add all the users using operator overloading.
"""


# creating a user account class
class UserAccount:
    def __init__(self, Uid, bal):
        self.Uid = Uid
        self.bal = bal

    def __add__(self, other):
        total_Uid = self.Uid + other.Uid
        total_bal = self.bal + other.bal
        return UserAccount(total_Uid, total_bal)


U1 = UserAccount(101, 50000)
U2 = UserAccount(102, 25000)
U3 = UserAccount(103, 75000)

print(U1 + U2 + U3)
