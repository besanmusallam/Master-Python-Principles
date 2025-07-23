from turtle import Turtle


MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, PADDLE_POSITION):
        super().__init__()
        self.create_paddle(paddle_position=PADDLE_POSITION)


    def create_paddle(self, paddle_position: list):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5) 
        self.setheading(UP)
        self.color("white")
        self.goto(paddle_position)

    def move(self):
        self.forward(MOVE_DISTANCE)
        

    def up(self):
        self.speed("fastest")
        if self.ycor() < 240:
            self.setheading(UP)
            self.move()
        


    def down(self):
        self.speed("fastest")
        if self.ycor() > -240:
            self.setheading(DOWN)
            self.move()