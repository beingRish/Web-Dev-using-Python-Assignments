'''
11. Write a python script to take the month value in numeric format and display the
number of days in it.
'''
month = int(input("Enter the month:"))
if month == 2:
    print("No of days:28/29 days")
elif month in (4, 6, 9, 11):
    print("No of days:30")
elif month in (1, 3, 5, 7, 8, 10, 12):
    print("No of days:31")
else:
    print("Wrong month")
