"""
9. Define a function which takes lengths of three sides of a triangle as arguments and
display the perimeter or triangle. Define and apply a decorator which checks for the
validity of the triangle on the basis of lengths of the side. This makes the perimeter to
be displayed when the triangle can exist with the given lengths of the sides.
"""


# defining the decorator
def decor_Tri(tri_func):
    def display(s1, s2, s3):
        if (s1 and s2 and s3) >= 100:
            print("This is large Triangle with enough length of sides")
        else:
            print("Does not exist the triangle which sides is smaller than 100")

    return display


# calling the decorator
@decor_Tri
# defining a function
def tri(s1, s2, s3):
    # operation to calculate perimeter
    peri = s1 + s2 + s3
    print("Perimeter of triangle=", peri)


# taking input from user
print("Enter three sides of Triangle:")
a, b, c = int(input()), int(input()), int(input())
# calling the function
tri(a, b, c)
