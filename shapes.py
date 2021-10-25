import turtle
import math

#2d Shapes
def circle(t: turtle.Turtle, r: float, color: str) -> None:
    """`shapes.circle`:
        Draw a circle with the provided dimensions
    Parameters:
        - `t` (turtle.Turtle):
            the turtle used to draw the shape
        - `r` (float):
            the radius of the circle
        - `color` (color):
            the color of the circle

    Notes:
        - side units are in pixels
    """
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    
def rectangle(t: turtle.Turtle, side1: float, side2: float, cornerOneAngle: float, cornerTwoAngle: float, right: bool, color: str) -> None:
    """`shapes.rectangle`:
        Draw a rectangle with the provided dimensions, corner angles, and color
    Parameters:
        - `t` (turtle.Turtle):
            the turtle used to draw the shape
        - `side1` (float):
            the length of the first (and third) side of the drawn rectangle
        - `side2` (float):
            the length of the second (and fourth) side of the drawn rectangle
        - `cornerOneAngle` (float):
            the angle of the first (and third) corner of the drawn rectangle
        - `cornerTwoAngle` (float):
            the angle of the second (and fourth) corner of the drawn rectangle
        - `right` (bool):
            the direction to turn on corners (True for right, False for left)
        - `color` (str):
            the color to make the inside of the square

    Notes:
        - side units are in pixels
        - angle units are in degrees
        - cornerOneAngle and cornerTwoAngle must add up to 180 in order to form an actual rectance
        - more info on colors can be found in the docs for turtle.Turtle.color()
        - yes I know if you set either of the corner angles not equal to 90 it's a parallelogram, but that's too long to type
    """
    t.color(color)
    t.begin_fill()
    for i in range(5): #loop fives times per rectangle to set up for the next face
        t.forward(side1 if i%2 == 0 else side2) #swap betweeen side lengths with modulo
        angle = cornerOneAngle if i%2 == 0 else cornerTwoAngle
        t.right(angle) if right else t.left(angle)
        if i == 3: t.end_fill() #fill in drawn rectangle after drawing 4 sides



#3d Shapes
def rectPrism(t: turtle.Turtle, l: float, w: float, h: float, colors: list) -> None:
    """`shapes.rectPrism`:
        Draw a rectangular prism with the provided dimensions and colors
    Parameters:
        - `t` (turtle.Turtle):
            the turtle object used to draw the shape
        - `l` (float):
            the length of the prism
        - `w` (float):
            the width of the prism
        - `h` (float):
            the height of the prism
        - `colors` (list):
            a list containing the colors for the first, second, and third faces of the prism

    Notes:
        - length, width, and height units are in pixels
        - colors should be formatted similarly to this: `colors=["red", "green", "blue"]
        """
    #scale the length to look proper on a 2d plain
    l /= 2
    #draw the front face
    rectangle(t, w, h, 90, 90, False, colors[0])
    #draw the right face
    rectangle(t, h, l, 45, 135, True, colors[1])
    #draw the upper face
    rectangle(t, l, w, -135, -45, True, colors[2])

def cube(t: turtle.Turtle, l: float, colors: list) -> None:
    """shapes.cube:
        draw a cube with the provided dimension and colors
    Parameters:
        - `t` (turtle.Turtle):
            the turtle object used to draw the shape
        - `l` (float):
            the size each side of the cube
        - `colors` (list):
            a list containing the colors for the first, second, and third faces of the prism
    Notes:
        - length unit is pixels
        - colors should be formatted similarly to this: `colors=["red", "green", "blue"]
    """
    rectPrism(t, l, l, l, colors)
