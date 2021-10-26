import turtle as trtl
import random
import math

# Screen width first tuple, second height

"""
drawer = trtl.Turtle()
drawer.setheading(135)
drawer.forward(20)
def bottom_draw(window_width):

    numOfLines = window_width / 12
"""    
trtl.shape('turtle')

def turtle_bounce(times):
    
    bouncyTurtle = trtl.Turtle()
    incrementer = 0
    screenSize = (trtl.screensize())
    MAX_X = screenSize[1]
    MAX_Y = screenSize[0]
    print(MAX_X, MAX_Y)

#    infinite = float('inf')
    turtle_colors = ["red", "green", "blue"]
    bouncyTurtle.shape('turtle')
    for color in turtle_colors:
        bouncyTurtle.color(color)
        #while incrementer < times:
            # bouncyTurtle.setheading(random.randint(90, 360))
        
        while incrementer < times:
        
            x_bouncyTurtle = bouncyTurtle.xcor()
            y_bouncyTurtle = bouncyTurtle.ycor()
            print(x_bouncyTurtle,y_bouncyTurtle)
            if abs(x_bouncyTurtle) >= MAX_X: # Use abs() to capture both walls
                bouncyTurtle.setheading(random.randint(90, 360))
                
            if abs(y_bouncyTurtle) >= MAX_Y:
                bouncyTurtle.setheading(random.randint(90, 360))
            bouncyTurtle.fd(1)

turtle_bounce(1)
             

winLoop = trtl.Screen()
winLoop.mainloop()
