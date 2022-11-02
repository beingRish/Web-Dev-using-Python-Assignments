# 10. Write a recursive python function to find the Nth term of the Fibonacci series.

# defining a function
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter a number:"))
print("Fibonacci series...")
for num in range(0, num):
    print(fibonacci(num), end=' ')
