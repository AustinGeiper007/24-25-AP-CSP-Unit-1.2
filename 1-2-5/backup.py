# Breakout

# Imports
import turtle as t
import random as rd

#-----Initialize Variables-----
score = 0
player_name = input("Input your name: ")

wn = t.Screen()
wn.colormode(255)

wn.bgcolor('black')

ball = t.Turtle()
ball.shape('circle')
ball.color(rd.randint(50,255),rd.randint(50,255),rd.randint(50,255))
ball.setheading(45)
ball.speed(3)
ball.penup()

paddle = t.Turtle()
paddle.speed('fastest')
paddle.penup()
paddle.color('white')
paddle.goto(0,-50)
paddle.shape('square')

#-----functions-----
def bounce_wall():
    if ball.heading() == 45:
        ball.left(90)
        ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
    elif ball.heading() == 135:
        ball.right(90)
        ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
    elif ball.heading() == 225:
        ball.left(90)
        ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
    elif ball.heading() == 315:
        ball.right(90)
        ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))

def bounce_ceiling():
    if ball.heading() == 45:
        ball.right(90)
        ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
    elif ball.heading() == 135:
        ball.left(90)
        ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))

def bounce_paddle():
    if ball.heading() == 225:
        ball.right(90)
    elif ball.heading() == 315:
        ball.left(90)

def loser():
    wn.mainloop()
def winner():
    print("yay")

def paddle_left():
    paddle.setheading(180)
    paddle.forward(2)
def paddle_right():
    paddle.setheading(0)
    paddle.forward(2)

#-----events-----

while True:
    ball.forward(2)
    wn.onkeypress(paddle_left, "a")
    wn.onkeypress(paddle_right, "d")
    wn.listen()
    if ball.xcor() <= -100 or ball.xcor() >= 100:
        bounce_wall()
    if ball.ycor() >= 250:
        bounce_ceiling()
    if ball.ycor() < -50:
        loser()
    if ball.ycor() <= 45:
        if ball.distance(paddle) <= 20:
            bounce_paddle()