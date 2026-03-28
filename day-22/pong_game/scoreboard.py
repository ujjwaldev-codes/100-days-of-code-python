from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.score1 =0
        self.score2 =0
        self.color("yellow")
        self.write(f"{self.score1}  {self.score2}",False, align="center", font=("Aerial",25 ,"normal"))
    def update_score(self,score1,score2):
        self.clear()
        self.score1=score1
        self.score2=score2
        self.write(f"{self.score1}  {self.score2}",False, align="center", font=("Aerial",25 ,"normal"))