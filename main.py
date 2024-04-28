import turtle


turtle.setup(500, 500, 0, 0)
turtle.screensize(480, 480, bg="#ccc")
turtle.tracer(0)

uzbek = turtle.Turtle()


def draw_square(x, y, length):
    uzbek.penup()
    uzbek.home()
    uzbek.goto((x, y))
    uzbek.color("red")
    uzbek.pendown()

    for storona in range(4):
        uzbek.forward(length)
        uzbek.right(90)


turtle.done()
