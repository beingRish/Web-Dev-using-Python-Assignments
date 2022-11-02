'''
10. Write a python program to create a function to check whether a given number is even
or odd.
'''


# defining function
def even_odd(n):
    print("Even") if n % 2 == 0 else print("Odd")


a = int(input("Enter a number:"))
even_odd(a)
