# 10. Write a recursive python function to print a number in reverse order

# defining a function
def reverse_order(n, r):
    if n == 0:
        return r
    else:
        return reverse_order(n//10, r * 10 + n % 10)


num = int(input("Enter a number: "))
print("Reversed number=", reverse_order(num, 0))
