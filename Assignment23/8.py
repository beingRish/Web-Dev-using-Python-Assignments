# 8. Create an endless iterator using generator method to produce Prime numbers

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def primeGenerator():
    num = 2
    while True:
        if isPrime(num):
            yield num
        num += 1
    return


it = primeGenerator()
prime_list = []
while True:
    ans = input("Do you want to generate another element[y/n] : ")
    if ans == 'y':
        x = next(it)
        print(x)
        prime_list.append(x)
    else:
        break
print(prime_list)
