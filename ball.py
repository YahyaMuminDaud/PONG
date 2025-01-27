from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid= 1)
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1
            

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce(self):
        self.ymove *= -1
        self.move_speed *= 0.9

    def paddle_bounce(self):
        self.xmove *= -1

    def reset_position(self):
        self.goto(0,0)      
        self.move_speed = 0.1
        self.paddle_bounce()