# 9. Write a python script to check whether a given year is a leap year or not
year = int(input("Enter a Year: "))
if year % 4 == 0 and year % 100 != 0:
    print("Leap year")
elif year % 400 == 0:
    print("Leap year")
else:
    print("Not Leap Year")
