'''
4. Write a python script to print all Prime numbers between two given numbers (both
values inclusive)
'''
lower = int(input("Enter the lower value:"))
upper = int(input("Enter the upper value:"))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=' ')
    
