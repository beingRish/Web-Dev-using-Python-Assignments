# 1. Use iter and next method to access all the elements of a given set using while loop.

# taking set element as input from user
s = input("Enter elements separated by comma:")
s1 = {eval(e) for e in s.split(',')}

# Accessing the elements of set through iter() method
it = iter(s1)
while len(s1):
    # printing the set element though next() method
    print(next(it), end=' ')

