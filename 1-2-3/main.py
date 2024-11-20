#   a123_apple_1.py
#-----setup-----
import turtle as trtl
import random as rand
from random import randint

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_drop_speed = 2.75 # Default to 2.75
apple_letter_x_offset = -25
apple_letter_y_offset = -50

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

lc_letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letter = 'a'

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(new_letter, active_apple):
  active_apple.showturtle()
  active_apple.shape(apple_image)
  draw_letter(new_letter, active_apple)
  wn.update()

# This function moves the apple to the ground and hides it.
def drop_apple():
  global apple_drop_speed, apple_letter_x_offset, apple_letter_y_offset
  wn.tracer(True)
  apple.speed(apple_drop_speed)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)


# letter is of type str
# active_apple is a turtle
def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 55, "bold"))
  active_apple.setpos(remember_position)


def reset_apple(apple):
  global lc_letters_list, letter
  if len(lc_letters_list) > 0:
      new_letter_id = randint(0, len(lc_letters_list) - 1)
      letter = lc_letters_list[new_letter_id]
      apple.penup()
      apple.goto(randint(-200, 200), 150)
      draw_apple(letter, apple)


#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
#for i in range(0, number_of_apples):
  #Your code here

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the
# apple and letter have dropped, call the apple resetting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

#-----function calls-----
draw_apple(letter, apple)
wn.onkeypress(drop_apple, str(letter))

wn.listen() # Tells the window to look for keypresses
wn.mainloop()