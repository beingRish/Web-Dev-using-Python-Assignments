"""
10. Define a function which calculates HCF of two numbers. Define and apply a
decorator to check whether two given numbers are co-prime or not.
"""


# defining the decorator
def decor_HCF(HCF_func):
    def coPrime(a, b):
        print("HCF =", HCF_func(a, b))
        if HCF_func(a, b) == 1:
            print("Co-Prime")
        else:
            print("Not Co-Prime")

    return coPrime


# calling the decorator
@decor_HCF
# defining a function
def cal_HCF(a, b):
    # Operation to calculate HCF
    while a % b != 0:
        rem = a % b
        a = b
        b = rem
    # returning the HCF value
    return b


# taking two numbers from user
print("Enter two number:")
x, y = int(input()), int(input())

# calling the function
cal_HCF(x, y)
