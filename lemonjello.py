from turtle import Turtle, Screen

class LemonJello(Turtle): # have to call the super class in the class line!
    # initial constructor
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('turtle')
        self.penup()
        self.seth(90)
        self.goto(0,-250)
        self.showturtle()


    def upmove(self):
        self.forward(25)


    def reset_position(self):
        self.goto(0, -250)