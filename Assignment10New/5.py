# 5. Write a python script to print table of user’s choice

choice = int(input("Enter a number:"))
for i in range(1, 11):
    print(choice, "*", i, "=", choice*i)
