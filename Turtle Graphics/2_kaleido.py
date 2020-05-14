import turtle as t
import time
from itertools import cycle

colors = cycle(['red', 'blue', 'green', 'yellow', 'orange', 'grey', 'purple', 'pink'])

def circle(size, angle, advance, shape):
    t.pencolor(next(colors))
    next_shape = ''
    if shape == 'circle':
        t.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        for i in range (4):
            t.forward(size * 2)
            t.left(90)
        next_shape = 'circle'
    
    t.right(angle)
    t.forward(advance)
    circle(size + 5, angle + 1, advance + 2, next_shape)


t.bgcolor('black')
t.speed('fast')
t.pensize(4)
circle(30, 0, 1, 'circle')

time.sleep(2)
t.hideturtle()
