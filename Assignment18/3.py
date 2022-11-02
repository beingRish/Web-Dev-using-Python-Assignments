# 3. Write a python program to get a list of the values from a dictionary.
day = int(input("How many days in a week:"))
d = {}
for e in range(day):
    key = int(input("Enter number of day:"))
    value = input("Enter day name:")
    d[key] = value
for e in d:
    print(e, d[e])

