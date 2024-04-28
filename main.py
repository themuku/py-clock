import turtle


turtle.setup(500, 500, 0, 0)
turtle.screensize(480, 480, bg="#ccc")
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



turtle.done()
