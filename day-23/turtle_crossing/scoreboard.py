FONT = ("Courier", 24, "normal")
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-210,250)
        self.level =1
        self.write(f"Level : {self.level}",False, align ="center",font = FONT)
    def update(self,arg):
        self.clear()
        if arg ==1:
            self.level+=1
            self.write(f"Level : {self.level}",False, align ="center",font = FONT)
        if arg ==0:
            self.goto(0,0)
            self.write(f"Game over at Level : {self.level}",False, align ="center",font = FONT)