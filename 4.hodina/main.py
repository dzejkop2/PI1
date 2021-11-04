import turtle
t = turtle.Turtle()
turtle.delay(10)
from random import randrange, uniform

t.pensize(5)

def trojuholnik(dlzkaA):
    t.pencolor("red")
    t.setheading(randrange(0,360))
    t.penup()
    t.setpos(randrange(-300,300), randrange(-300,300))
    t.pendown()
    for z in range(3):
        t.forward(dlzkaA)
        t.left(120)

def stvorec(dlzkaB):
    t.pencolor("blue")
    t.setheading(randrange(0, 360))
    t.penup()
    t.setpos(randrange(-300, 300), randrange(-300, 300))
    t.pendown()
    for i in range(4):
        t.forward(dlzkaB)
        t.right(90)

for i in range(randrange(1,10)):
    trojuholnik(randrange(50,100))
    stvorec(randrange(50,100))

turtle.exitonclick()