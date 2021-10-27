import turtle

def gradient(t: turtle.Turtle, startingRGB: int, endingRGB: int, h: float, w: float) -> None:
    t.pensize(1)
    turtle.colormode(255)
    t.setheading(90)
    for i in range(w):
        rgb = int((endingRGB-startingRGB)*(i/w) + startingRGB)
        t.color((255, rgb, rgb))
        t.forward(h) if i%2 == 0 else t.backward(h)
        t.goto(t.xcor()+1, t.ycor())
