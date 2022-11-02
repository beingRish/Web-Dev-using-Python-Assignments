# 5. Create a generator to produce first n terms of Fibonacci series

def fibonacciGenerator(n):
    a, b = 0, 1
    while n:
        yield a
        a, b = b, a + b
        n -= 1


for e in fibonacciGenerator(int(input("Enter a number:"))):
    print(e, end=' ')
