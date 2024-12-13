# Breakout

# Imports
import turtle as t
import random as rd

# -----Initialize Variables-----
score = 0
player_name = input("Input your name: ")

# Recommended Values: 250, -100, 100, -51, 2
ceiling_height = 250
left_wall = -100
right_wall = 100
void_pos = -51
ball_speed = 2

# draws the walls that define the space played in
wall_painter = t.Turtle()
wall_painter.speed(0)
wall_painter.penup()
wall_painter.hideturtle()
wall_painter.color('white')
wall_painter.pensize(2)
wall_painter.goto(left_wall, void_pos)
wall_painter.pendown()
wall_painter.goto(left_wall, ceiling_height)
wall_painter.goto(right_wall, ceiling_height)
wall_painter.goto(right_wall, void_pos)
wall_painter.color('red')
wall_painter.goto(left_wall, void_pos)

#  lets us use rgb values on the screen
wn = t.Screen()
wn.colormode(255)

wn.bgcolor('black')

# creates the bouncing ball
ball = t.Turtle()
ball.shape('circle')
ball.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
ball.setheading(45)
ball.speed(3)
ball.penup()

# makes the paddle that the player controls
paddle = t.Turtle()
paddle.speed(0)
paddle.penup()
paddle.color('white')
paddle.goto(0, void_pos - 1)
paddle.shape('square')

# starts workin with the score
score_trtl = t.Turtle()
score_trtl.penup()
score_trtl.speed(0)
score_trtl.color('white')
score_trtl.goto(-300, -200)
score_trtl.hideturtle()

# List of brick coords
brick_line_1 = [(-80, 225), (-60, 225), (-40, 225), (-20, 225), (0, 225), (20, 225), (40, 225), (60, 225), (80, 225)]
brick_line_2 = [(-60, 175), (-40, 175), (-20, 175), (0, 175), (20, 175), (40, 175), (60, 175)]
brick_line_3 = [(-40, 125), (-20, 125), (0, 125), (20, 125), (40, 125)]

brick_trtl_list = []

# Creates Turtles
for num in range(9):
    brick = t.Turtle()
    brick.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
    brick.penup()
    brick.speed(0)
    brick.shape('square')
    brick.goto(brick_line_1[num])
for num in range(7):
    brick = t.Turtle()
    brick.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
    brick.penup()
    brick.speed(0)
    brick.shape('square')
    brick.goto(brick_line_2[num])
for num in range(5):
    brick = t.Turtle()
    brick.color(rd.randint(50, 255), rd.randint(50, 255), rd.randint(50, 255))
    brick.penup()
    brick.speed(0)
    brick.shape('square')
    brick.goto(brick_line_3[num])


# -----functions-----
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
    print("Congrats,", player_name, ". You broke all the bricks!!")


def paddle_left():
    paddle.setheading(180)
    paddle.forward(5)


def paddle_right():
    paddle.setheading(0)
    paddle.forward(5)


def score_up_one():
    global score
    score += 1
    score_trtl.clear()
    score_trtl.write("Score: " + str(score), font=("Helvetica", 32, "bold"))


def brick_broken():
    print("brick")
    brick.hideturtle()
    if brick.ycor() == 225:
        brick_line_1.remove((brick.xcor(), brick.ycor()))
    if brick.ycor() == 175:
        brick_line_2.remove((brick.xcor(), brick.ycor()))
    if brick.ycor() == 125:
        brick_line_3.remove((brick.xcor(), brick.ycor()))


# -----events-----

while True:
    # Move the ball
    ball.forward(ball_speed)

    # Paddle movement events
    wn.onkeypress(paddle_left, "a")
    wn.onkeypress(paddle_right, "d")
    wn.onkeypress(paddle_left, "Left")
    wn.onkeypress(paddle_right, "Right")

    # This is temporary and for testing purposes only
    wn.onkeypress(score_up_one, "Up")

    wn.listen()

    # Checking position of ball
    if ball.xcor() <= left_wall or ball.xcor() >= right_wall:
        bounce_wall()
    if ball.ycor() >= ceiling_height:
        bounce_ceiling()
    if ball.ycor() <= void_pos:
        loser()
    if ball.ycor() <= 45:
        if ball.distance(paddle) <= 20:
            bounce_paddle()
    if ball.distance(brick) <= 20:
        brick_broken()