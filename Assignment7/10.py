'''
10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
    a. Yellow - Monday
    b. Blue - Tuesday
    c. Orange - Wednesday
    d. White - Thursday
    e. Black - Friday
    f. Red - Saturday
    g. All other colours - Sunday
'''
colour = input("Enter Your Favorite colour: ")

match colour:
    case colour if 'yellow' in colour:
        print("Monday")
    case colour if 'blue' in colour:
        print("Tuesday")
    case colour if 'orange' in colour:
        print("Wednesday")
    case colour if 'white' in colour:
        print("Thursday")
    case colour if 'black' in colour:
        print("Friday")
    case colour if 'red' in colour:
        print("Saturday")
    case _:
        print("Sunday")
