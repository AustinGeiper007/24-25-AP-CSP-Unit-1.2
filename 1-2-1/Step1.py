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

#-----game functions--------
def spot_clicked(x, y):
    print("HELLO WORLD!!!")

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()