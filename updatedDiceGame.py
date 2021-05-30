
'''
==================================
ColorScheme Dice Roll Pictuanary
Created by: Yuliya Vaskiv
Date: 05/27/2021
...................................

The dice game that requires
user input on how many dices to roll.
The number on dice is randomly picked by app
and those number are presented on picture
in each round with different color


==============================================

Notes:
The app can still use modifications toward
the graphing each square that represent number on dice.
Because rows and columns are changing each time
depending on the roll for dice
05/27/2021
'''

import random
import turtle


def gameO():
    print('---------------------------')
    a = int (input ("Dice(s) to roll?: "))
    return a


def createList(diceRoll):
    l = []
    for i in range (diceRoll):
        r = random.randint(1, 6)
        l.append(r)
    return l


    
def drawSquares(t, l, pointA, pointB, rowCount, size, color):


    totalColumntLength = int ((len(l) / rowCount) + 1)
    
    column = int((len(l) / totalColumntLength))
    
    for j in range (len(l)):
        
        t.speed(0.00001)

        for p in range(1000):
            if j == column * p:
                if (pointA == 0 and pointB == 0):
                    pointA = pointA
                    pointB = pointB
                    
                pointA = pointA + ( 6 * size) + size
                pointB = pointB + (column * size) 
            

        for k in range(l[j]):
            
            xDistr = k * size + pointA
            yDistr = pointB - j * size

            t.color('grey')
            t.up()
            t.goto(xDistr , yDistr)
            t.down()

            
            t.fillcolor(color)
            t.begin_fill()

            for side in range(4):
                t.forward(size)
                t.right(90)
            t.end_fill()


                
'''==========================================================='''
print ("Welcome to Dice Representation")
print ("To stop the game press key 0")

colorList = ['black', 'red', 'blue', 'purple', 'yellow', 'green', 'orange',
             'black', 'red', 'blue', 'purple', 'yellow', 'green', 'orange',
             'black', 'red', 'blue', 'purple', 'yellow', 'green', 'orange']
tu = turtle.Turtle()

run = 0
flag = True
x = -600
y = 50
while flag == True:
    diceToRoll = gameO()
    if diceToRoll  == 0:
        flag = False
    else:
        rollList = (createList(diceToRoll))
        print(rollList)

        drawSquares(tu, rollList, x, y, 10, 30, colorList[run])
        run = run + 1


    





