from turtle import Turtle
from random import randint, choice

COLOURS = ['cyan', 'pink', 'green', 'red', 'blue', 'yellow', 'orange']


class Car(Turtle):
    """Instantiate car. Inherits from Turtle() class."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.setheading(180)
        self.shapesize(1, 2)
        self.penup()
    
    def create_car(self):
        """Assign an unique possition an colour attributs to each car."""
        car_position = randint(-250, 250)
        car_colour = choice(COLOURS)
        self.color(car_colour)
        self.goto(280, car_position)
        self.showturtle()
        
    def move(self):
        """Move car a random quantity of pixels forward."""
        distance_forward = randint(4, 20)
        self.forward(distance_forward)
