from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.cars = []
    

    def create_car(self):
        new_car = Turtle('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(300,random.randint(-220,260))
        self.cars.append(new_car)
        

    def move(self):
        for car in self.cars:
            if car.xcor() > -320:
                new_x = car.xcor() - 5
                car.goto(new_x, car.ycor())
