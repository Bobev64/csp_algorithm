import turtle
import math
painter = turtle.Turtle()
painter.penup()
painter.goto(-200, -200)
painter.pendown()
painter.speed(0)
painter.color("blue")
painter.hideturtle()

print(painter.xcor(), painter.ycor())

def rectPrism(l: float, w: float, h: float, colors: list) -> None:
    painter.color(colors[0])
    painter.begin_fill()
    painter.setheading(0)
    for i in range(2):
        painter.forward(w)
        painter.left(90)
        painter.forward(h)
        painter.left(90)
    painter.end_fill()

    painter.forward(w)
    painter.color(colors[1])
    painter.begin_fill()
    painter.setheading(90)
    painter.forward(h)
    painter.setheading(45)
    painter.forward(l/2)
    painter.setheading(270)
    painter.forward(h)
    painter.setheading(225)
    painter.forward(l/2)
    painter.end_fill()
    
    painter.setheading(90)
    painter.forward(h)
    painter.color(colors[2])
    painter.begin_fill()

    painter.setheading(180)
    painter.forward(w)
    painter.setheading(45)
    painter.forward(l/2)
    painter.setheading(0)
    painter.forward(w)
    painter.end_fill()
    painter.penup()
    painter.goto(-200, -200)

def cube(l, colors) -> None:
    rectPrism(l, l, l, colors)
    
for i in range(100, 300, 10):
    cube(i, ["red", "green", "blue"])
    #painter.clear()


wn = turtle.Screen()
wn.mainloop()
