import turtle

def rectPrism(t: turtle.Turtle, l: float, w: float, h: float, colors: list) -> None:
    t.color(colors[0])
    t.begin_fill()
    t.setheading(0)
    for i in range(5):
        t.forward(w if i%2 == 0 else h)
        t.left(90)
        if i == 3: t.end_fill()

    t.color(colors[1])
    t.begin_fill()
    for i in range(5):
        t.forward(h if i%2 == 0 else l/2)
        t.right(45 if i%2 == 0 else 135)
        if i == 3: t.end_fill()

    t.color(colors[2])
    t.begin_fill()
    for i in range(3):
        t.forward(l/2 if i%2 == 0 else w)
        t.right(-135 if i%2 == 0 else -45)
    t.end_fill()
    t.penup()

def cube(t: turtle.Turtle, l: float, colors: list) -> None:
    rectPrism(t, l, l, l, colors)
