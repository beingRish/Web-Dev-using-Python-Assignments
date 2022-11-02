'''
10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.
'''
print("Enter three numbers:")
a, b, c = int(input()), int(input()), int(input())
'''if a == b == c:
    print(a or b or c, "is equal.")
elif b < a > c:
    print(a, "is greater.")
elif b > c:
    print(b, "is greater.")
else:
    print(c, "is greater.")
'''

print((a if a > c else c) if a > b else (b if b > c else c))
