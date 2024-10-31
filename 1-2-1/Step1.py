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

timer = 30
counter_interval = 1000 #1000 is equal to 1 second
timer_up = False

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

counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.speed(0)
counter.goto(-450, 350)
counter.pendown()

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
    global timer_up
    if timer_up == False:
        update_score()
        change_position()
    elif timer_up == True:
        spot.hideturtle()
    else:
        print("Error. Reboot...")

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
'''Field size testing code. Removed comments if use needed.
Used to determine size of area spot can move too. Very crude methodology'''
'''
spot.speed(0)
spot.pendown()
while True:
    change_position()
'''
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()