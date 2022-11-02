# 5. Write a Python script to append list of city names in a file ‘cities.txt’.

with open('cities.txt', 'a') as f:
    f.write(" Jaipur Mumbai London")
