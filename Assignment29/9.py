"""
9. Write a Python script to store book data in a file. Book data is in the form of a
dictionary in which book name is the key and price is its value. Use pickle to store
data into a file (say bookfile)
"""
import pickle

book = {
    'WINGS OF FIRE': 154,
    'The Teacher I Never Met': 175,
    'Agni Ki Udaan': 331,
    'How To Win Your Life': 539,
    'Agnipankh': 324
    }
f = open('bookfile', 'ab')
pickle.dump(book, f)
f.close()

