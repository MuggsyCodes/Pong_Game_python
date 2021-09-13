from turtle import Turtle, Screen

class Paddle(Turtle): # have to call the super class in the class line!
    # initial constructor
    def __init__(self, pad_position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pad_position)

    def upmove(self):
        self.seth(90)
        self.forward(20)
        self.seth(0)


    def downmove(self):
        self.seth(270)
        self.forward(20)
        self.seth(0)

# # Turtle paddle object
# paddle = Turtle(shape='square')
# paddle.color('white')
# paddle.penup()
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.setposition(x=350, y=0)
#
#



