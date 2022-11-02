# 3. Write a python script to print all Prime numbers under 100
for i in range(1, 101):
    c = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c = c + 1
    if c == 2:
        print(i, end=' ')
    c = 0
