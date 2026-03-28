COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random 
class CarManager():
    # while is_game_on:
    def __init__(self):
        self.speed = MOVE_INCREMENT
        self.all_cars=[]
    def create_car(self):
        car = Turtle("square")
        car.hideturtle()
        if random.randint(1,7)==1:
            car.showturtle()
            car.color(random.choice(COLORS))
            car.penup() 
            car.goto(300,random.randint(-250,280))
            car.shapesize(stretch_len=2, stretch_wid=1)
            self.all_cars.append(car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)
            # car.
    def update_speed(self):
            #increase the speed of car
            self.speed+=5

