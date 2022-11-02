# 6. Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or not

def searching(filename, city):
    try:
        f = open(filename, 'r')
        for line in f.readlines():
            strlist = line.split(' ')
            for w in strlist:
                if city == w:
                    return True
        else:
            return False
        f.close()
    except FileNotFoundError:
        print("File doesn't exist")


city_name = input("Enter the city name you want to search:")
result = searching('cities.txt', city_name)
if result:
    print("Yes", city_name, "is present in the file.")
else:
    print("No", city_name, "is not present in the file.")

