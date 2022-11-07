# 2020/02/18

from turtle import Turtle, Screen, colormode
import random
timmy = Turtle()
# timmy.shape('turtle')
timmy.color('green')
# timmy.pensize(1)
timmy.speed(0)
screen = Screen()
colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)
timmy.penup()
# timmy.setx(-250)
# timmy.sety(-250)
for i in range(10):
    timmy.color(random_color())
    timmy.setx(-250)
    timmy.sety(-250)
    timmy.setheading(90)
    timmy.forward(50*(i))
    timmy.setheading(0)
    for j in range(10):
        timmy.dot(20,random_color())
        timmy.forward(50)
screen.exitonclick()