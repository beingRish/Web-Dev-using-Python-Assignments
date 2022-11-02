# 8. Write a recursive python function to print binary of a given decimal number.

# defining a function
def bin_num(n):
    if n == 0:
        return 0
    else:
        bin_num(n // 2)
        print(n % 2, end='')


# calling the function
num = int(input("Enter a number:"))
bin_num(num)
