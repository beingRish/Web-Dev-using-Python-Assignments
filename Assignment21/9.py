# 9. Write a recursive python function to print first N multiples of a given number.

# defining a function
def N_Multiples(n1, n2):
    if n1 > 0:
        N_Multiples(n1-1, n2)
        print(n1*n2)


# taking input from user
num1 = int(input("Enter a number till you want to get multiple:"))
num2 = int(input("Enter a number which you want to get multiple:"))

# calling the function
N_Multiples(num1, num2)
