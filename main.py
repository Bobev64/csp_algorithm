import shapes
import turtle

painter = turtle.Turtle()
painter.speed(1)

shapes.cube(painter, 100, colors = ["red", "green", "blue"])
wn = turtle.Screen()
wn.mainloop()
