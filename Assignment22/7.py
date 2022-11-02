# 7. Write a recursive python function to calculate sum of the digits of a given number.

def sumDig(n):
    if n % 10 == 0:
        return 0
    else:
        s = n % 10 + sumDig(n // 10)

    return s


num = int(input("Enter a number:"))
print("Sum of digits=", sumDig(num))
