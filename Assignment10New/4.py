# 4. Write a python script to print the first 10 multiples of N in reverse order.
n = int(input("Enter Value:"))
for i in range(10, 0, -1):
    print(n*i, end=' ')

