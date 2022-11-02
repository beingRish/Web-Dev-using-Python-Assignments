# 7. Write a Python script to remove all non int values from a list.
a = [1, 2, "hello", 3.5, "my", 5.5, True, 5 + 6j]
b = []
for i in a:
    if type(i) == int:
        b.append(i)
a = b
print(a)
