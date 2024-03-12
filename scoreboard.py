from turtle import Turtle

ALINGN = 'center'
FONT = ('verdana', 12, 'normal')

class LevelBanner(Turtle):
    """Instantiate level banner. Inherits from Turtle()."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color('black')

    def refresh_level(self, level):
        """Update level after player's turtle reach top of the window."""
        self.clear()
        self.color('blue')
        self.write(f"Level: {level}",
                   align=ALINGN, font=FONT)

    def game_over(self):
        """Write game over message on window if player hits car."""
        self.goto(0, 0)
        self.clear()
        self.write(f"**** GAME OVER ****",
                       align=ALINGN, font=('verdana', 18, 'normal'))

    def quit_game(self):
        """Write message on window if player press 'q' key'."""
        self.goto(0, 0)
        self.clear()
        self.color('red')
        self.write(f"**** GAME ENDED WITH CRASH ****",
                       align=ALINGN, font=('verdana', 18, 'normal'))
        
    def winner(self):
        """Write winners message if player reach level 12."""
        self.goto(0, 0)
        self.clear()
        self.color('red')
        self.write(f"**** Level 12 - YOU WIN!!! ****",
                   align=ALINGN, font=('verdana', 18, 'normal'))
        