"""
In this project I have got oppertunity to make/code for Snake Game though simple, yet the world's most famous and legendary childhood game of many.
I was supposed to complete this in two days.


Features or working of the program :
1.) Body and ground of snake
2.) Detection logic for touching a wall or its own body to lose, or randomly appearing fruit/food
to increase its body size and scre.
4.) It shall be controlled by arrows and conitnuously move as set its heading.
5.) More the score, winner is the player.(Higher scores need better control since body size grows and result in quicker end of game by eating its own body)


"""
from scoreboard import ScoreBoard
from turtle import Screen
from snake import Snake
from food import Food
import time
#object creation
screen = Screen()
#screen setup
screen.setup(width = 600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
#body of the snake
snake=Snake()
food = Food()
#move the snake automatically
# tracer takes the number and turn the program on or off
# animation, update the screen each time changes take place
screen.tracer(0)
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

game_is_on=True
score=ScoreBoard()
while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        #Detect collision with food
        if(snake.segments[0].distance(food)<15):
                food.reappear()
        # Managed to show and update score on scoreboard using turtle only 
                score.update_score(1)
                snake.grow()
        #detection of collison with walls 
        # size increase and score increase
        if(snake.segments[0].xcor()<-295 or snake.segments[0].ycor()<-285 or snake.segments[0].xcor()>280 or snake.segments[0].ycor()>285):
                score.update_score(0)
                game_is_on=False
        #detection its own tail
        #we avoid having game over in the beginning due to checking distance of snake's head from its head(first body segments) to be less than 10
        # for index in range(1,len(snake.segments)-1):
                # if snake.segments[0].distance(snake.segments[index])<15:
                #         score.update_score(0)
                #         game_is_on=False    
        #used slicing to make it better work with less code
        for segment in snake.segments[1:]:
                if snake.segments[0].distance(segment)<15:
                        score.update_score(0)
                        game_is_on=False
screen.exitonclick()
