import turtle
import time

my_turtle = turtle.Turtle()

def drawside(length,angle):
    my_turtle.forward(length)
    my_turtle.left(angle)


def rectangle1():
    i = 0
    while i <= 3:
        if i == 0 or i == 2:
            drawside(300,90)
            i += 1
        elif i == 1 or i == 3:
            drawside(225,90)
            i += 1

def rectangle2():
    i = 0
    while i <= 3:
        if i == 1 or i == 3:
            drawside(100, 90)
            i += 1
        elif i == 0 or i == 2:
            drawside(75, 90)
            i += 1

def triangle():
    i = 0
    while i <= 2:
        if i ==0:
            drawside(300,140)
            i += 1
        elif i == 1:
            drawside(195,80)
            i +=1
        elif i == 2:
            drawside(195,230)
            i += 1

def rectangle3():
    i = 0
    while i <= 2:
        if i == 1:
            drawside(65, 90)
            i += 1
        elif i == 0:
            drawside(125, 90)
            i += 1
        elif i == 2:
            drawside(75, 90)
            i += 1

my_turtle.penup()
my_turtle.goto(-200,-100)
my_turtle.pendown()

rectangle1()

my_turtle.penup()
my_turtle.goto(-75,-100)
my_turtle.pendown()

rectangle2()

my_turtle.penup()
my_turtle.goto(-200,125)
my_turtle.pendown()

triangle()

my_turtle.penup()
my_turtle.goto(90,135)
my_turtle.pendown()

rectangle3()

time.sleep(3)