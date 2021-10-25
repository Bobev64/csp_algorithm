import shapes
import turtle

painter = turtle.Turtle()
painter.speed(0)

shapes.circle(painter, 100, "blue")
wn = turtle.Screen()
wn.mainloop()
