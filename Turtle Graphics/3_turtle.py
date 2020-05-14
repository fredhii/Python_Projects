import turtle as t
import random
import time


def inside_win():
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 100
    (x, y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside

def move_turtle():
    if inside_win():
        angle = random.randint(0, 180)
        dist = random.randint(50, 200)
        t.right(angle)
        t.forward(dist)
    else:
        t.backward(180)

t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('slowest')


while True:
    move_turtle()

time.sleep(5)