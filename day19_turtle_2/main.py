# 2020/02/19

from turtle import Turtle, Screen

color_list = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title='Make your bet', prompt= 'Which wurtle will win the race? Enter a color: ')


for i in range(0,6):
    tim = Turtle('turtle')
    tim.color(color_list[i])
    tim.penup()
    tim.goto(x=-230, y=-150 + (i*60))


screen.exitonclick()