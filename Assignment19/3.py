"""
3. Write a python program to create a function which expects an unknown number of
arguments.
"""


# defining a function with variable length argument
def name(*t):
    print(t)


# function calling
name("Rishabh")
name("Shubham", "Sagar")
name("Bandana", "Mony", "Neha", "Khushboo", "Lovely", "Siddhi")
name("Shivam", "Ranjay", "Suman", "Vikash")
