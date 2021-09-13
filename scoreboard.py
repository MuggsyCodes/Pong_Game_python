from turtle import Turtle

FONT = ('Courier', 24, 'normal')



class Scoreboard(Turtle):  # have to call the super class in the class line!
    # initial constructor
    def __init__(self):
        super().__init__()
        self.color('black')
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-200, 200)
        self.write(f'Level: {self.level}', align='center', font= FONT)


    def level_up(self):
        self.level += 1
        self.clear()
        self.goto(-200, 200)
        self.write(f'Level: {self.level}', align='center', font= FONT)

    def game_over_text(self):
        self.clear()
        self.goto(0, 0)
        self.write('GAME OVER HOMBRE', align='center', font= FONT)
