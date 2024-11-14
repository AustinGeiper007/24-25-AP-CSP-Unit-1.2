#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file
apple = trtl.Turtle()

apple_fall_speed = 1

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def apple_down(active_apple):
  global apple_fall_speed
  active_apple.penup()
  xcor = active_apple.xcor()
  ycor = active_apple.ycor()
  ycor -= apple_fall_speed
  active_apple.goto(xcor, ycor)

#-----function calls-----
draw_apple(apple)
while True:
  apple_down(apple)
wn.mainloop()