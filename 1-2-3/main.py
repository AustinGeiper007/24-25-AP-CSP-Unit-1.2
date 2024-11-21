#   a123_apple_1.py
#-----setup-----
import turtle as trtl
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
apple_letters = ['a']

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
  apple_letters.pop()
  wn.tracer(False)
  reset_apple(apple)


# active_apple is a turtle
def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 55, "bold"))
  active_apple.setpos(remember_position)


def reset_apple(apple):
  global lc_letters_list
  if len(lc_letters_list) > 0:
      new_letter_id = randint(0, len(lc_letters_list) - 1)
      apple_letters.append(lc_letters_list[new_letter_id])
      apple.penup()
      apple.goto(randint(-200, 200), 150)
      draw_apple(apple_letters[0], apple)

# Here are all the checks for letters
# Very Brute force, very lengthy
def check_apple_a():
    if 'a' in apple_letters:
        drop_apple()

def check_apple_b():
    if 'b' in apple_letters:
        drop_apple()

def check_apple_c():
    if 'c' in apple_letters:
        drop_apple()

def check_apple_d():
    if 'd' in apple_letters:
        drop_apple()

def check_apple_e():
    if 'e' in apple_letters:
        drop_apple()

def check_apple_f():
    if 'f' in apple_letters:
        drop_apple()

def check_apple_g():
    if 'g' in apple_letters:
        drop_apple()

def check_apple_h():
    if 'h' in apple_letters:
        drop_apple()

def check_apple_i():
    if 'i' in apple_letters:
        drop_apple()

def check_apple_j():
    if 'j' in apple_letters:
        drop_apple()

def check_apple_k():
    if 'k' in apple_letters:
        drop_apple()

def check_apple_l():
    if 'l' in apple_letters:
        drop_apple()

def check_apple_m():
    if 'm' in apple_letters:
        drop_apple()

def check_apple_n():
    if 'n' in apple_letters:
        drop_apple()

def check_apple_o():
    if 'o' in apple_letters:
        drop_apple()

def check_apple_p():
    if 'p' in apple_letters:
        drop_apple()

def check_apple_q():
    if 'q' in apple_letters:
        drop_apple()

def check_apple_r():
    if 'r' in apple_letters:
        drop_apple()

def check_apple_s():
    if 's' in apple_letters:
        drop_apple()

def check_apple_t():
    if 't' in apple_letters:
        drop_apple()

def check_apple_u():
    if 'u' in apple_letters:
        drop_apple()

def check_apple_v():
    if 'v' in apple_letters:
        drop_apple()

def check_apple_w():
    if 'w' in apple_letters:
        drop_apple()

def check_apple_x():
    if 'x' in apple_letters:
        drop_apple()

def check_apple_y():
    if 'y' in apple_letters:
        drop_apple()

def check_apple_z():
    if 'z' in apple_letters:
        drop_apple()

#-----function calls-----
draw_apple(apple_letters[0], apple)
# All keypress functions
# Very brute force
wn.onkeypress(check_apple_a, 'a')
wn.onkeypress(check_apple_b, 'b')
wn.onkeypress(check_apple_c, 'c')
wn.onkeypress(check_apple_d, 'd')
wn.onkeypress(check_apple_e, 'e')
wn.onkeypress(check_apple_f, 'f')
wn.onkeypress(check_apple_g, 'g')
wn.onkeypress(check_apple_h, 'h')
wn.onkeypress(check_apple_i, 'i')
wn.onkeypress(check_apple_j, 'j')
wn.onkeypress(check_apple_k, 'k')
wn.onkeypress(check_apple_l, 'l')
wn.onkeypress(check_apple_m, 'm')
wn.onkeypress(check_apple_n, 'n')
wn.onkeypress(check_apple_o, 'o')
wn.onkeypress(check_apple_p, 'p')
wn.onkeypress(check_apple_q, 'q')
wn.onkeypress(check_apple_r, 'r')
wn.onkeypress(check_apple_s, 's')
wn.onkeypress(check_apple_t, 't')
wn.onkeypress(check_apple_u, 'u')
wn.onkeypress(check_apple_v, 'v')
wn.onkeypress(check_apple_w, 'w')
wn.onkeypress(check_apple_x, 'x')
wn.onkeypress(check_apple_y, 'y')
wn.onkeypress(check_apple_z, 'z')

wn.listen() # Tells the window to look for keypresses
wn.mainloop()