from turtle import Turtle

START_LINE = (0, -280)
Y_FINISH_LINE = 280

class Player(Turtle):
    """Instantiate player's turtle.Inherits from Turtle class."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.goto(START_LINE)
        self.showturtle()
        self.move = 10

    def move_turtle(self):
        """Move turtle up if correct key is presse key='Up'."""
        if self.ycor() > 280:
            self.goto(START_LINE)
        y_cor= self.ycor() + self.move
        self.sety(y_cor)
