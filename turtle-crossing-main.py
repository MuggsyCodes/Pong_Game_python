from turtle import Turtle, Screen
from lemonjello import LemonJello
from car import Car
from scoreboard import Scoreboard
import threading
import time

# Turtle crossing initialisation

screen = Screen()
lemonjello = LemonJello()

scoreboard = Scoreboard()

screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Turtle crossing')
screen.listen()

screen.onkey(lemonjello.upmove, "Up")

game_is_on = True
j = 0
s = 20 # initial speed
while game_is_on:
    # update screen based on delay
    time.sleep(0.1)
    screen.update()
    #generate a new car every 6th loop iteration
    # keep track of loops and % 6 == 0
    if j % 6 == 0:
        car = Car() # create new car object
        car.move_car(car,s) # move all cars forward
    # Detect collision
    if car.crash_detect(lemonjello) == False:
        game_is_on = False
        scoreboard.game_over_text()
        # detect turtle crosses road
    if lemonjello.ycor() > 290:
        # reset position and increase while loop speed
        lemonjello.reset_position()
        scoreboard.level_up()
        s+=10
    j+=1
screen.exitonclick()
