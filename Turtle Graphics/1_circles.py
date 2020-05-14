import turtle as t
import time
from itertools import cycle

colors = cycle(['red', 'blue', 'green', 'yellow', 'orange', 'grey', 'purple', 'pink'])

def circle(size, angle, advance):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(advance)
    circle(size + 5, angle + 2, advance + 5)


t.bgcolor('black')
t.speed('fast')
t.pensize(4)
circle(30, 0, 1)

time.sleep(2)
t.hideturtle()