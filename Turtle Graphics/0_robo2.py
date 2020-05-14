import turtle as t
import time

def rectangle(hor, ver, col):
    t.pendown()
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for i in range(1, 3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')

''' =============================== '''
''' Create Foot '''
''' =============================== '''
t.goto(-100, -150)
rectangle(50, 20, 'silver')
t.goto(-30, -150)
rectangle(50, 20, 'silver')

''' =============================== '''
''' Create Leg '''
''' =============================== '''
t.goto(-25, -50)
rectangle(15, 100, 'grey')
t.goto(-55, -50)
rectangle(-15, 100, 'grey')

''' =============================== '''
''' Create Torso '''
''' =============================== '''
t.goto(-90, 100)
rectangle(100, 150, 'silver')

''' =============================== '''
''' Create Arm '''
''' =============================== '''
t.goto(-150, 70)
rectangle(60, 15, 'grey')
t.goto(-150, 110)
rectangle(15, 40, 'grey')
t.goto(10, 70)
rectangle(60, 15, 'grey')
t.goto(55, 110)
rectangle(15, 40, 'grey')

''' =============================== '''
''' Create Head '''
''' =============================== '''
t.goto(-50, 120)
rectangle(15, 20, 'grey')
t.goto(-85, 170)
rectangle(80, 50, 'silver')
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-60, 160)
rectangle(5, 5, 'black')
t.goto(-40, 155)
rectangle(5, 5, 'black')
t.goto(-65, 138)
rectangle(40, 5, 'black')
t.right(5)

''' =============================== '''
''' Create Hand '''
''' =============================== '''
t.goto(-155, 130)
rectangle(25, 25, 'silver')
t.goto(-147, 130)
rectangle(10, 15, t.bgcolor())
t.goto(50,130)
rectangle(25, 25, 'silver')
t.goto(58, 130)
rectangle(10, 15, t.bgcolor())


t.hideturtle()
time.sleep(10)
t.hideturtle()