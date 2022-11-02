"""
4. Write a python script to create two Threads. First thread will print all Even numbers
and Second thread will print all Odd numbers till 100.
"""
from time import sleep
from threading import Thread


class EvenNumbers(Thread):
    def Even(self):
        for i in range(1, 101):
            if i % 2 == 0:
                print(i)
                # sleep(1)


class OddNumbers(Thread):
    def Odd(self):
        for i in range(1, 101):
            if i % 2 != 0:
                print(i)
                # sleep(1)


e = EvenNumbers()
o = OddNumbers()

e.Even()
o.Odd()
