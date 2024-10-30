# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = 'blue'
spot_size = 2
spot_shape = 'circle'

score_color = 'black'
font_setup = "Arial", 20, "normal"

score = 0
written_score = "Score: " + str(score)

#-----initialize turtle(s)-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.color(spot_color)
spot.penup()

score_writer = trtl.Turtle()
score_writer.color(score_color)
score_writer.penup()
score_writer.speed(0)
score_writer.goto(350, 350)
score_writer.hideturtle()

#-----game functions--------
def change_position():
    new_xpos = rand.randint(-450, 450)
    new_ypos = rand.randint(-375, 300)
    spot.goto(new_xpos, new_ypos)

def update_score():
    global score
    global written_score
    score_writer.clear()
    score += 1
    written_score = "Score: " + str(score)
    score_writer.write(written_score, font=font_setup)

def spot_clicked(x, y):
    update_score()
    change_position()

#-----events----------------
'''Field size testing code. Removed comments if use needed
spot.speed(0)
spot.pendown()
while True:
    change_position()'''
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()