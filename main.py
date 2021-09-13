from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def pong():
    # Screen events
    screen = Screen()
    screen.tracer(0)
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    # screen.screensize(canvwidth=800, canvheight=600, bg='black') # note: Angela uses setup
    screen.title('Pong')
    screen.listen()

    r_paddle = Paddle((350,0))
    l_paddle = Paddle((-350, 0))

    ball = Ball()

    scoreboard = Scoreboard()

    screen.onkey(r_paddle.upmove, "Up")
    screen.onkey(r_paddle.downmove, "Down")

    screen.onkey(l_paddle.upmove, "w")
    screen.onkey(l_paddle.downmove, "s")

    game_is_on = True
    a = 1
    b = 1
    wall = 280
    n = 1 # iniital ball speed
    ball.speed(n)
    i = ball.loop_speed
    print(i)
    while game_is_on:
            time.sleep(i)
            # print('first line')
            screen.update()
            x1, y1 = ball.coords()
            ball.ball_move_2(a,b)
            x2, y2 = ball.coords()
            dx = x2 - x1
            dy = y2 - y1
            if ball.ycor() > wall or ball.ycor() < -wall:
                a, b = ball.bounce(dx, dy)
            # Detect collision with r_paddle
            if ball.distance(r_paddle) < 20 or ball.distance(l_paddle) < 20:
                print("Right or Left Paddle collision")
                a, b = ball.paddle_bounce(dx)
                i = ball.run_speed()
                print(f'loop speed: {ball.run_speed}')
            elif ball.xcor() > 330 and ball.distance(r_paddle) < 50:
                print("top side R Paddle collision")
                a, b = ball.paddle_bounce(dx)
                i = ball.run_speed()
            elif ball.xcor() < -330 and ball.distance(l_paddle) < 50:
                print("top side L Paddle collision")
                a, b = ball.paddle_bounce(dx)
                ball.ball_speed()
            elif ball.xcor() > 360: # left player gets point
                print("Ball out of RIGHT bounds")
                scoreboard.a_point(dx)
                a = ball.reset_position(dx)
                time.sleep(1)
            elif ball.xcor() < -360: # right player gets point
                print("Ball out of LEFT bounds")
                scoreboard.a_point(dx)
                a = ball.reset_position(dx)
                time.sleep(1)
            print(f'loop speed {ball.loop_speed}')
    screen.exitonclick()

pong()