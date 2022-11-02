# 4. Create a generator to produce squares of first N natural numbers.

def squareGenerator(n):
    x = 1
    while n:
        yield x * x
        x += 1
        n -= 1


for e in squareGenerator(int(input("Enter a number:"))):
    print(e, end=' ')
