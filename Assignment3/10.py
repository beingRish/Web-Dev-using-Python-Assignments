'''
10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
display the result in binary format.
'''
o = 0o25
h = 0x39
Result = bin(o) +  bin(h)
print("Result in Binary=", Result)