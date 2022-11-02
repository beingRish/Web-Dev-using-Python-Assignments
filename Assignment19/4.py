# 4. Write a python program to create a function which expects kwargs arguments

# defining a function
def information(name, age, course, college):
    print('Name=', name, '\nAge=', age, '\nCourse=', course, '\nCollege=', college)


# calling the function which accepts keyword arguments
information('Rishabh', college='COC', age=24, course='MCA')
