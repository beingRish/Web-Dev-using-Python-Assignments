'''
12. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part
'''
c = complex(input("Enter a Complex Number:"))
print(type(c))
print(c)
print("Real part=", c.real)
print("Imaginary part=", c.imag)
if c.real > c.imag:
    print("Real part is greater")
else:
    print("Imaginary part is greater")
