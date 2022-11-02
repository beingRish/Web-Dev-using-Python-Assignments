'''
3. Write a menu-driven program with the following options:
      a. Check whether a given set of three numbers are lengths of an isosceles
         triangle or not
      b. Check whether a given set of three numbers are lengths of sides of a right-angled
         triangle or not
      c. Check whether a given set of three numbers are equilateral triangle or not
      d. Exit.
'''
print("Press a for check lengths of an isosceles triangle")
print("Press b for check lengths of sides of a right-angled triangle")
print("Press c for check equilateral triangle or not")
print("Press d for Exit")
c = input("Enter a choice:")
match c:
    case 'a':
        print("Enter three sides:")
        s1, s2, s3 = int(input()), int(input()), int(input())
        if s1 == s2 or s1 == s3 or s2 == s3:
            print("All the three numbers are lengths of an isosceles triangle")
        else:
            print("All the three numbers are not lengths of an isosceles triangle")
    case 'b':
        print("Enter three sides:")
        a, b, c = int(input()), int(input()), int(input())
        if (a*a + b*b == c*c) or (c*c + b*b == a*a) or (a*a + c*c == b*b):
            print("Right-Angled Triangle")
        else:
            print("Not Right-Angled Triangle")
    case 'c':
        print("Enter three sides:")
        a, b, c = int(input()), int(input()), int(input())
        if a==b==c:
            print("It is a equilateral triangle")
        else:
            print("It is not an equilateral triangle")
    case 'd':
        exit("Exit")
    case other:
        print("invalid operation")