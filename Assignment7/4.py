'''
4. Write a program which takes user’s age and display the category of person. Age
below 10 years-Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.
'''
age = int(input("Enter Age:"))

match age:
    case age if age < 10:
        print("Kid")
    case age if age < 20:
        print("Teen")
    case age if age < 40:
        print("Young")
    case age if age < 60:
        print("Experienced")
    case age if age > 60:
        print("Senior Citizen")
    case other:
        print("Try Another Choice")
