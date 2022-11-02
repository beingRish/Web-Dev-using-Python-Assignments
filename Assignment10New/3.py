# 3. Write a python script to print first M multiples of N.

m, n = int(input("Enter Value:")), int(input("Enter Value"))
for i in range(1, m+1):
    print(n*i, end=' ')
