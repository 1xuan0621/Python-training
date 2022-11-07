import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

carmanager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')


def gameover():
    global game_is_on
    game_is_on = False
screen.onkey(gameover, 'c')


count = 0
game_is_on = True
while game_is_on:
    count += 1
    time.sleep(player.level)
    screen.update()
    scoreboard.update()
    
    if count % 4 == 0:
        carmanager.create_car()    
    carmanager.move()

    if player.ycor() > 300:
        player.level_up()
        scoreboard.level_up()

    for car in carmanager.cars:
        if player.distance(car) < 20:
            screen.update()
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()