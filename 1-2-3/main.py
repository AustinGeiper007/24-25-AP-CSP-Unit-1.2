#   a123_apple_1.py
import turtle as trtl
import random as rd

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file
apple = trtl.Turtle()

apple_fall_speed = 2.75 # Default is 2.75 (decimals work)
ground_height = -200 # Default is -200

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_apple():
  apple.penup()
  apple.speed(apple_fall_speed)
  apple.goto(apple.xcor(), ground_height)

#-----function calls-----
draw_apple(apple)
wn.onkeypress(drop_apple, "a")

wn.listen() # Tells the window to look for keypresses

wn.mainloop()