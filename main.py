import shapes
import gradients
import turtle

painter = turtle.Turtle()
painter.speed(0)
painter.hideturtle()

painter.penup()
painter.goto(-350, -350) #Move turtle to ensure rainbow is centered on screen
painter.pendown()

gradients.multiGradient(painter, #Draw Background Rainbow
    [[255, 0, 0],   #Red
    [255, 165, 0],  #Orange
    [255, 255, 0],  #Yellow
    [0, 255, 0],    #Green
    [0, 0, 255],    #Blue
    [128, 0, 128]], #Purple
    700, 700, 0)

painter.penup()
painter.goto(-50, -50) #Move turtle to center cube on screen
painter.pendown()

shapes.cube(painter, #draw cube in the center
    100, #set cube size to 100px
    ["red", "green", "blue"] #Cube faces will be red, green, and blue
)

wn = turtle.Screen()
wn.mainloop()
