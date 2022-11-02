# 5. Write a python script to print two given words in dictionary order
'''w1 = input("Enter first word: ")
w2 = input("Enter second word: ")
if w1 > w2:
    print(w1, w2)
else:
    print(w2, w1) '''

print("Enter two Words: ")
a, b = input(), input()
print((b, a) if a > b else (a, b))
