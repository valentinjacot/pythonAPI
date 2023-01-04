import math
import numpy
import random

door1=door2=door3="goat"

def assign():
    #num=random.randrange(0,1000)
    num=1
    if num<333:
        door1="car"
    elif num<666:
        door2="car"
    else:
        door3="car"

#def choose():

win=0
loose=0

for i in range(1000):
    num2=random.randrange(0,1000)
    if num2>666:
        #open door2, make choice
        win+=1
    elif num2>333:
        #open door3, make choice
        win+=1
    else:
        loose+=1


print("number of win : " + str(win))
print("number of loose : " + str(loose))




