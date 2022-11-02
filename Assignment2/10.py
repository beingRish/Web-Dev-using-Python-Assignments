'''
10. Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)
'''
import datetime
d = datetime.datetime.now()
print("Current Date and Time is:", d.strftime('%d-%m-%Y %H:%M %p'))