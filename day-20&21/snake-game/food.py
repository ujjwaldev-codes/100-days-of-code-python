from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.color("red")
        self.goto(random.randint(-270,270),random.randint(-270,270))
    def reappear(self):
        self.goto(random.randint(-270,270),random.randint(-270,270))



        # day-20&21/Snake_Game