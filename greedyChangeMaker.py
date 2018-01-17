#Greedy algorithm converted to python
import sys
import os
import decimal

c = float(input("How much change is owed? "))
c = round(c * 100)
i = 0
while (c<0 or c==0):
    print("Please input a positive amount...")
    
while (c>24):

    i  += 1
    c=(c-25)

while (c>=10):

    i += 1
    c=(c-10)


while (c>=5):

    i += 1
    c=(c-5)


while (c>=1):

    i += 1
    c=(c-1)

print("%i coin(s) needed to make the change." % i)