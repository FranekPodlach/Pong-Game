from turtle import Turtle

POSITIONS_Y = [-40, -20, 0, 20, 40]


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.x_position = x_position
        self.shape("square")
        self.turtlesize(5, 1, 1)
        self.penup()
        self.speed(0)
        self.color("white")
        self.goto(x_position, 0)

    def up(self):
        self.goto(self.x_position, self.ycor() + 20)

    def down(self):
        self.goto(self.x_position, self.ycor() - 20)
        


