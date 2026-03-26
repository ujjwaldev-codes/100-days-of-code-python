from turtle import Turtle, Screen
START_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
class Snake:
        def __init__(self):
            self.segments=[]
            def create_snake(self):
                for positions in START_POSITION:
                    self.add_segment(positions)
            create_snake(self)
        def move(self):
            for seg_num in range(len(self.segments)-1,0,-1):
                        new_x=self.segments[seg_num -1].xcor()
                        new_y=self.segments[seg_num -1].ycor()
                        self.segments[seg_num].goto(new_x,new_y)
            self.segments[0].forward(MOVE_DISTANCE)
        #self.segments[0] is head of snake
        def add_segment(self,positions):
            self.segment= Turtle("square")
            self.segment.penup()
            self.segment.color("white")
            self.segment.goto(positions)
            self.segments.append(self.segment)
        def up(self):
            if(self.segments[0].heading()!=270):
                self.segments[0].seth(90)
        def down(self):
            if(self.segments[0].heading()!=90):
                self.segments[0].seth(270)
        def left(self):
            if(self.segments[0].heading()!=0):
                self.segments[0].seth(180)
        def right(self):
            if(self.segments[0].heading()!=180):
                self.segments[0].seth(0)
        def grow(self):
             #negative number so that it counts from end of the list
             #Also using turtle 's module's Turtle class method position()
             self.add_segment(self.segments[-1].position())
             
              
