from turtle import Turtle, Screen
import paddle
import ball
import time
import scoreboard
#SCREEN SETUP
screen = Screen()
screen.setup(width=900,height=600)
screen.bgcolor("black")
def middle_white_line():
    tim = Turtle()
    tim.hideturtle()
    tim.penup()
    tim.goto(0,300)
    tim.pencolor("white")
    tim.pendown()
    tim.pensize(3)
    tim.goto(0,-300)
middle_white_line()
screen.listen()
screen.tracer(0)
paddle1 = paddle.Paddle(1)
paddle2 =paddle.Paddle(-1)
score = scoreboard.ScoreBoard()
screen.onkey(paddle2.up,"w")
screen.onkey(paddle1.up,"Up")
screen.onkey(paddle2.down,"s")
screen.onkey(paddle1.down,"Down")
ball = ball.Ball()
is_game_on=True
score1 =0
score2 =0
# Moving and bouncing logic, bounce only when touch up and down, sidesways only if touched paddle else it will be miss
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bouce_upper_wall_move()
    # also increase the speed every time paddles hit the ball
    if ball.distance(paddle2)<50 and ball.xcor()<-410 or ball.distance(paddle1)<50 and ball.xcor()>410:
        ball.paddle_hit_move()
        ball.move_speed*=0.8
    #condition of win and lose and score board
    if ball.xcor()<=-500:
        score2+=1
        ball.reset()
    if ball.xcor()>=500:
        score1+=1
        ball.reset()
    score.update_score(score1,score2)
screen.exitonclick()
