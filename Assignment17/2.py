# 2. Write a python program to store your own information {name, age, gender, so on..}

# taking information from user
info = input("Enter your information:")

information = {eval(e) for  e in info.split(',')}
print(information)
