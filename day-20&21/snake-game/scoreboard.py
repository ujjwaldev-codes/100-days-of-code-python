import turtle as t
ALIGN ="center"
FONT =("Aerial",20,"normal")
class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        # self.score =t.Turtle("square")
        self.penup()
        self.points=0
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.write(f"Score : {self.points}",align=ALIGN,font=FONT)
    def update_score(self,signal):
        if(signal==1):
            self.clear()
            self.points +=1
            self.write(f"Score : {self.points}",align=ALIGN,font=FONT)
        if(signal==0):
            self.clear()
            self.write(f"Final Score : {self.points}",align=ALIGN,font=FONT)
            self.goto(0,0)
            self.write("GAME OVER !!!",align=ALIGN,font=FONT)

        