"""
3. Write a python program to create a function that prints the even numbers from a
given list.
Sample_List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


# defining a function
def evenList():
    # creating a list
    Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # operation to check even or odd
    for e in range(len(Sample_List)):
        if Sample_List[e] % 2 == 0:
            print(Sample_List[e])


# calling the function
evenList()
