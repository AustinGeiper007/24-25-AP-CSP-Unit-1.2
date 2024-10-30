# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = 'blue'
spot_size = 2
spot_shape = 'circle'

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.color(spot_color)
spot.penup()

#-----game functions--------
def change_position():
    new_xpos = rand.randint(-450, 450)
    new_ypos = rand.randint(-375, 375)
    spot.goto(new_xpos, new_ypos)

def spot_clicked(x, y):
    change_position()

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()