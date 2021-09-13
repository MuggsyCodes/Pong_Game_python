from turtle import Turtle, Screen
import time

X_MOVE = 10
Y_MOVE = 8

class Ball(Turtle): # have to call the super class in the class line!
    # initial constructor
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.loop_speed = 0.1


    def ball_move(self):
        xc = self.xcor()
        yc = self.ycor()
        self.speed(1)
        self.goto(xc+X_MOVE, yc+Y_MOVE)

    def ball_move_2(self, a, b):
        xc = self.xcor()
        yc = self.ycor()
        self.goto(xc+a*X_MOVE, yc+b*Y_MOVE)

    def run_speed(self):
        self.loop_speed *= 0.9
        return self.loop_speed

    def coords(self):
        x1 = self.xcor()
        y1 = self.ycor()
        # print(f'x {x1}, y {y1}')
        return x1, y1

    def bounce(self, dx, dy):
        if dx > 0:  # (Moving RT)
            if dy > 0:  # UP & RT
                print('up & right')
                a = 1
                b = -1
                return a, b
            else:  # dy < 0 # DWN & RT
                a = 1
                b = 1
                return a, b
        else:  # dx < 0 (Moving LT)
            if dy > 0:  # UP & LT
                print('up & left')
                a = -1
                b = -1
                return a, b
            else:  # dy < 0 # DWN & LT
                print('down & left')
                a = -1
                b = 1
                return a, b

    def paddle_bounce(self, dx):
        # Right paddle strike
        if dx > 0:
            print(f'turtle speed: {self.speed()}')
            a = -1
            b = 1
            return a, b
        if dx < 0: # Left paddle strike
            print(f'turtle speed: {self.speed()}')
            a = 1
            b = 1
            return a, b

    def reset_position(self, dx):
        print('reset position')
        self.goto(0, 0)
        self.loop_speed = 0.1
        print('reset loop speed')
        if dx > 0: # ball hit RIGHT wall
            a = -1
            return a
            # self.ball_move_2(-1, 1)
        else:
            a = 1
            return a

    def ball_speed(self): # input starting speed
        current = self.speed()
        current +=1
        self.speed(current)
        print(f'new ball speed: {self.speed()}')