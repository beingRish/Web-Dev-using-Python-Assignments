"""
7. Write a Python script to count the number of Python keywords occurring in a python
source file.
"""

import keyword
k = keyword.kwlist
print(k)
f = open('6.py', 'r')
word_count = 0
for words in f.readlines():
    strlist = words.split(' ')
    for i in range(len(strlist)):
        for j in range(len(k)):
            if strlist[i] == k[j]:
                word_count += 1
print(word_count)
f.close()


