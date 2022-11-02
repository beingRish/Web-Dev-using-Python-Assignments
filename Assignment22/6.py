# 6. Write a recursive python function to calculate the factorial of a number

# defining function
def Calculate_Factorial(n):
    if n == 1:
        return 1
    else:
        f = n * Calculate_Factorial(n-1)

    return f


num = int(input("Enter a number:"))
print("Factorial of", num, "is", Calculate_Factorial(num))
