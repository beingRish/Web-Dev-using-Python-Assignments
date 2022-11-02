# 6. Create a generator to produce first n prime numbers

def primeGenerator(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


for e in primeGenerator(int(input("Enter a number:"))):
    print(e, end=' ')
