import turtle
import time

myturtle = turtle.Turtle()

def draw2sides(x):
    i = 0
    while i <= 1:
        myturtle.right(90)
        myturtle.forward(x)
        i = i + 1


def drawloop(y):
    i = 0
    x = 10
    while i <= y:
        draw2sides(x)
        i = i + 1
        x = x + 5

drawloop(17)

time.sleep(5)