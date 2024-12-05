import turtle as trtl
import random as rand

# Intialize Variables
wn = trtl.Screen()
maze_painter = trtl.Turtle()
wall_len = 35
path_width = 30



# Setup Turtle
maze_painter.left(90)
maze_painter.pensize(5)
maze_painter.color('black')
maze_painter.penup()
maze_painter.speed(0)

# Draw Maze
# Process:
# Draw a line
# Turn Left
# Increment Length
# Repeat
def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)

#just so there isn't a random blip in the beginning
maze_painter.penup()

for wall in range(21):
    # Gen Rand
    if(wall > 5):
        door = rand.randint(path_width * 2, (wall_len - path_width * 2))
        barrier = rand.randint(path_width * 2, (wall_len - path_width * 2))
    else:
        door = wall_len / 3
    # Beginning of wall
    maze_painter.forward(wall_len / 3)
    # Making door
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    if(wall > 5):
        draw_barrier()
    # Remaining wall
    maze_painter.forward(wall_len - path_width - (wall_len / 3))
    # setup next wall
    maze_painter.left(90)
    wall_len += 15








wn.listen()
wn.mainloop()