import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
player = Player()
screen.tracer(0)
screen.listen()
car = CarManager()
screen.onkey(player.move,"Up")
game_is_on = True
index =0
car = CarManager()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    #Dtect collision with blocks(hurdles)and game over ! 
    for cars in car.all_cars:
        if player.distance(cars)<25 and player.ycor()<300:
            screen.clear()
            scoreboard.update(0)
            game_is_on=False
    #increase the level and their speed, increase
    if player.ycor()>=300:
        scoreboard.update(1)
        player.reset()
        car.update_speed()
    index +=1
screen.exitonclick()
# Found making multiple cars to move x-coordinate
