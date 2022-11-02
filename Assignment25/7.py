"""
7. Write a python script to create a Phone class with 2 methods to print the features
(calling and sms).
"""


class Phone:
    @staticmethod
    def calling():
        print("You can Call after dialing the number.")

    @staticmethod
    def sms():
        print("You can text after typing something.")


p = Phone()
p.calling()
p.sms()
