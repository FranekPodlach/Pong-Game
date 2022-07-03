from turtle import Turtle 


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_distance = 10
        self.y_distance = 10

    def move(self):
        self.goto(self.xcor() + self.x_distance, self.ycor() + self.y_distance)

    def bounce_y(self):
        self.y_distance *= -1
        
    def bounce_x(self):
        self.x_distance *= -1
    
    def reset(self):
        self.home()
        self.bounce_x()