"""
Understanding the coordinate system in Turtle.
Learnt the teaching from my instructor : Expand the solutions and combine and reproduce new possibilities and make it better expand donot be limited and satisfied by solution codes.
"""
from turtle import Turtle, Screen
import random
screen =Screen()
screen.setup(width = 500, height=400)
user_choice = screen.textinput(title="Make your coice",prompt='Which colour ("red", "yellow", "blue","violet", "green") Turtle will win the race :  ')
tim = Turtle(shape="turtle")
jhon = Turtle(shape="turtle")
timmy = Turtle(shape="turtle")
jhonny = Turtle(shape="turtle")
rishu=Turtle(shape="turtle")
tim.color("red")
timmy.color("yellow")
jhon.color("green")
jhonny.color("violet")
rishu.color("blue")
# setup() --> set up the height and width of the screen
# textinput() --> need input title and prompt take input in graphic vicual form not terminal
# Here we prefer positional arguments
print("\n\nYou Chose "+user_choice+" Turtle")
# goto() --> can put turtle to its position, but how to know the x and y value of desired position.
tim.penup()
timmy.penup()
jhon.penup()
jhonny.penup()
rishu.penup()
tim.goto(x =-240 , y=0 ) # -250 is just behind screen, so just right adn also it is ovbious now that centre is origin
tim.goto(x=-240, y=80)
timmy.goto(x=-240, y=0)
jhon.goto(x=-240, y=-80)
jhonny.goto(x=-240, y=160)
rishu.goto(x=-240, y=-160)
candidates =[tim,timmy,jhon,jhonny,rishu]
steps=[1,2,3,4,5,6,7,8,9,10]
race_status ="on"
# Logic of random winning by varying their speed
#inital line is at x= -240 and final line is at x = 225
while race_status=="on":
    current_runner = random.choice(candidates)
    current_runner.forward(random.choice(steps))
    for turtles in candidates:
        if turtles.xcor()>220:
            race_status="off"
            if turtles.pencolor()==user_choice:
                print("\nYou won the bet !!!")
            else:
                print("\nYou lost the bet !!!")
            print(f"\n{turtles.pencolor()} Turtle won the race...\n")
        
            
screen.exitonclick()
