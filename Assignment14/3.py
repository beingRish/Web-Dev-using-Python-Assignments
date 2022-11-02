# 3. Write a Python script to create a list of first N even natural numbers.
n = int(input("Enter a number:"))
even = list(range(2, n + 1, 2))
print(even)
