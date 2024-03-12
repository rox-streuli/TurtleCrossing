from turtle import Turtle, Screen
from random import randint
import time
from player import Player
from scoreboard import LevelBanner
from car_manager import Car

LEVEL = 1
LEVEL_SPEED = 0.4
HEIGHT= 600
WIDTH = 600
NUMBER_OF_CARS = 4
GAME_ON = True

# Instantiate window
window = Screen()
window.setup(width=WIDTH, height=HEIGHT)
window.bgcolor('lightgrey')
window.title("Turtle Crossing")

# Instantiate level banner
level_banner = LevelBanner()

# Instantiate player's turtle
player = Player()

def exit_game():
    """Freze cars and print quit_game message."""
    window.resetscreen()
    level_banner.quit_game()
    time.sleep(5)
    window.bye()


# turn off tracer
window.tracer(0)

# listen for key event
window.listen()

# Collect key-events from player turtle
window.onkey(player.move_turtle, key='Up')

# collect event for finish game
window.onkey(exit_game, key='q')

counter = 0
list_of_cars = []

while GAME_ON:
    if counter % 20 == 0:
        # Create cars at the right of the screen and append to list.
        for i in range(randint(1, NUMBER_OF_CARS)):
            new_car = Car()
            new_car.create_car()
            list_of_cars.append(new_car)
    # detect successful crossing of road and increase level
    if player.ycor() > 280:
        LEVEL += 1
        LEVEL_SPEED *= 0.9
        # exit game and print banner if level 12 reached
        if LEVEL == 12:
            level_banner.winner()
            GAME_ON = False

    time.sleep(LEVEL_SPEED)
    counter += 1
    level_banner.refresh_level(LEVEL)
    window.update()
    # move cars on list forward
    for car in list_of_cars:
        if car.xcor() > -280:
            car.move()
            # detect turtle crash with car
            if car.distance(player) < 20:
                # game over
                level_banner.game_over()
                GAME_ON = False
        else:
            # Delete car if reach windows left side
            car.hideturtle()
            list_of_cars.remove(car)

       
window.exitonclick()
