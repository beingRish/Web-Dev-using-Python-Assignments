# 1. Write a python script to display the number of days in a given month number

'''
month = int(input("Enter month number: "))
match month <= 12:
    case 1:
        print("No of days: 31")
    case 2:
        print("No of days: 28/29")
    case 3:
        print("No of days: 31")
    case 4:
        print("No of days: 30")
    case 5:
        print("No of days: 31")
    case 6:
        print("No of days: 30")
    case 7:
        print("No of days: 31")
    case 8:
        print("No of days: 31")
    case 9:
        print("No of days: 30")
    case 10:
        print("No of days: 31")
    case 11:
        print("No of days: 30")
    case 12:
        print("No of days: 31")
    case other:
        print("Invalid Month")

'''

# Saurabh Sir
month = int(input("Enter month number:"))
match month:
    case month if month in (1, 3, 5, 7, 8, 10, 12):
        print("31 Days")
    case month if month in (4, 6, 9, 11):
        print("30 Days")
    case 2:
        print("28 or 29 Days")
    case _:
        print("Invalid Month number")
print()
