# 9. Write a recursive python function to print octal of a given decimal number

# defining a function
def oct_num(n):
    if n == 0:
        return 0
    else:
        oct_num(n // 8)
        print(n % 8, end='')


# calling the function
num = int(input("Enter a number:"))
oct_num(num)
