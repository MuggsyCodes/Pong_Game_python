from turtle import Turtle, Screen
import random

COLORS = ['red', 'green', 'yellow', 'blue', 'purple', 'orange', 'steelblue']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10 # Increases every time player levels up

Rx = 300 # start turtle at x = 300
car_list = []


class Car(Turtle): # have to call the super class in the class line!
    # initial constructor
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.seth(180)
        self.goto(Rx, random.randint(-250, 250))
        self.showturtle()


    def move_car(self, car_obj, s):
        car_list.append(car_obj)  # add car object to list of cars
        for car in car_list:
            car.forward(s)


    def crash_detect(self, turtle_obj):
        for auto in car_list:
            d = turtle_obj.distance(auto)
            if d < 10:
                print("Crash!")
                return False





