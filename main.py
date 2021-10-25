import cubes
import turtle

painter = turtle.Turtle()
painter.speed(0)

cubes.cube(painter, 100, colors = ["red", "green", "blue"])
wn = turtle.Screen()
wn.mainloop()
