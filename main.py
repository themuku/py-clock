import turtle
from datetime import datetime


screen = turtle.Screen()
screen.setup(500, 500, 0, 0)
screen.screensize(480, 480, bg="#ccc")
turtle.tracer(0)

uzbek = turtle.Turtle()


def draw_lines(length, rotation):
    uzbek.penup()
    uzbek.home()
    uzbek.color("black")
    uzbek.pensize(1)
    uzbek.right(rotation)
    uzbek.forward(170)
    uzbek.pendown()
    uzbek.forward(length)
    uzbek.penup()



def draw_watchface():
    uzbek.penup()

    for i in range(0,360,30):
        draw_lines(20, i)

    for i in range(0,360,6):
        draw_lines(10, i)

    uzbek.penup()
    

def draw_hands(length, rotation):
    uzbek.penup()
    uzbek.home()
    uzbek.pensize(2)
    uzbek.right(1* rotation + 90 * 3)
    uzbek.pendown()
    uzbek.forward(length)
    uzbek.penup()


def draw_time(h, m, s):
    uzbek.penup()
    uzbek.goto(-220, -220)
    uzbek.pendown()
    formatted_time = f"{h}:{m}:{s}"
    uzbek.color("white")
    uzbek.write(formatted_time, move=False, align="left", font=("Arial", 16, "normal"))
    uzbek.penup()


while True:
    time = datetime.now()

    hours = time.hour
    minutes = time.minute
    seconds = time.second

    uzbek.clear()
    draw_watchface()
    uzbek.color("blue")
    draw_hands(100, hours * 30)
    uzbek.color("red")
    draw_hands(130, minutes * 6)
    uzbek.color("green")
    uzbek.pensize(3)
    draw_hands(160, seconds * 6)

    draw_time(hours, minutes, seconds)

    screen.update()
    