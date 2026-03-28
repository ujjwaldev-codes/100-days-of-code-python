from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,arg):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape("square")
        # by default turtle object is of size 20x20
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(430*arg,0)
    def up(self):
        self.goto(self.xcor(),self.ycor()+40)
    def down(self):
        self.goto(self.xcor(),self.ycor()-40)
    