import turtle

def rectPrism(painter: turtle.Turtle, l: float, w: float, h: float, colors: list) -> None:
    painter.color(colors[0])
    painter.begin_fill()
    painter.setheading(0)
    for i in range(5):
        painter.forward(w if i%2 == 0 else h)
        painter.left(90)
        if i == 3: painter.end_fill()

    painter.color(colors[1])
    painter.begin_fill()
    for i in range(5):
        painter.forward(h if i%2 == 0 else l/2)
        painter.right(45 if i%2 == 0 else 135)
        if i == 3: painter.end_fill()

    painter.color(colors[2])
    painter.begin_fill()
    for i in range(3):
        painter.forward(l/2 if i%2 == 0 else w)
        painter.right(-135 if i%2 == 0 else -45)
    painter.end_fill()
    painter.penup()

def cube(painter: turtle.Turtle, l: float, colors: list) -> None:
    rectPrism(painter, l, l, l, colors)
