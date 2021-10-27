import shapes
import gradient
import turtle

painter = turtle.Turtle()
painter.speed(1)
shapes.cube(painter, 100, ["red", "green", "blue"])
painter.penup()
painter.goto(0, 0)
painter.pendown()
gradient.gradient(painter, 0, 255, 100, 100)
#gradient.gradient(painter, 0, 255, 600, 600)

wn = turtle.Screen()
wn.mainloop()
