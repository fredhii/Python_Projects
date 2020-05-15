import turtle as t
import random
import time

t.bgcolor('yellow')

""" ========================================================================== """
""" CREATE GAME ELEMENTS """
""" ========================================================================== """
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.hideturtle()

text_turtle = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align = 'center', font = ('Arial', 18, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

""" ========================================================================== """
""" GAME LOGIC """
""" ========================================================================== """
def outisde_window():
    left_win = -t.window_width() / 2
    right_win = t.window_width() / 2
    top_win = t.window_height() / 2
    bottom_win = -t.window_height() / 2    
    (x, y) = caterpillar.pos()
    outside = x < left_win or x > right_win or y > top_win or y < bottom_win
    return outside

def place_leaf():
    leaf.hideturtle()
    leaf.penup()
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.showturtle()

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER', align = 'center', font = ('Arial', 30, 'bold'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 30
    y = (t.window_height() / 2) - 60
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align='right', font = ('Arial', 35, 'bold'))

def start_game():
    game_status = True
    score = 0
    text_turtle.clear()

    caterpillar_speed = 1
    caterpillar_length = 2
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length += 0.5
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed += 0.5
            score += 10
            display_score(score)
        if outisde_window():
            game_over()
            break

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)


""" ========================================================================== """
""" HANDLE KEY INPUTS """
""" ========================================================================== """
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')
t.listen()
t.mainloop()