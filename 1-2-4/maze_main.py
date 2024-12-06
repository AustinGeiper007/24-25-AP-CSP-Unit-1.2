import turtle as trtl
import random as rand

# Initialize Variables
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
    global wall_len, door, barrier, path_width
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)

def draw_door():
    global path_width
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()

def first_5_iterations():
    global door, wall_len, path_width
    door = wall_len / 3
    maze_painter.forward(wall_len / 3)
    draw_door()
    maze_painter.forward(wall_len - path_width - (wall_len / 3))

def barrier_first():
    global wall_len, door, barrier, path_width
    maze_painter.forward(barrier)
    draw_barrier()
    maze_painter.forward(door - barrier)
    draw_door()
    maze_painter.forward(wall_len - barrier - (door - barrier) - path_width)

def door_first():
    global wall_len, door, barrier, path_width
    maze_painter.forward(door)
    draw_door()
    maze_painter.forward(barrier - door - path_width)
    draw_barrier()
    maze_painter.forward(wall_len - door - (barrier - door - path_width) - path_width)

#just so there isn't a random blip in the beginning
maze_painter.penup()

for wall in range(33):
    # Gen Rand
    if wall > 5:
        door = rand.randint(path_width, (wall_len - path_width))
        barrier = rand.randint(path_width, (wall_len - path_width))
        if door > barrier:
            barrier_first()
        elif door < barrier:
            door_first()
        else:
            first_5_iterations()

    else:
        first_5_iterations()

    # setup next wall
    maze_painter.left(90)
    wall_len += 15








wn.listen()
wn.mainloop()