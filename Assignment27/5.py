# 5. Write a python script to handle multiple Exception in one try.

try:
    a, b = int(input("Enter first number:")), int(input("Enter second number:"))

    c = a/b
    print(c)

    if a > b:
        print(a, "is greater than", b)
    else:
        print(b, "is greater than", a)

    print('Rishabh'+b)

except TypeError:
    print("Tum String ko Integer ke sath nahi jod sakte ho")

except ValueError:
    print("Are Gadhe! Tum String q Enter kr rhe ho jab operation integers ka krna hai to?")

except ZeroDivisionError:
    print("Ab se kv v 0 se divide nahi krna")

