import turtle as trtl
import random
import math

'''
This program is meant to take the turtle object and bounce it
around the boundaries of the screen when it hits a boundary
it also is meant to change color each time it hits a given border
and only increment a certain amount of times.
'''

trtl.shape('turtle')

def turtle_bounce(times):
    
    bouncyTurtle = trtl.Turtle()
    incrementer = 0
    screenSize = (trtl.screensize())
    MAX_X = screenSize[1]
    MAX_Y = screenSize[0]
    print(MAX_X, MAX_Y)

    # Initializing colors to pass to the turtle object, meant to change upon each bounce
    turtle_colors = ["red", "green", "blue"]
    bouncyTurtle.shape('turtle')
    for color in turtle_colors: # Should change color per bounce
        bouncyTurtle.color(color)
        # bouncyTurtle.setheading(random.randint(90, 360))
        
        # While loop should execute number of times you want turtle to bounce
        while incrementer < times:
        
            x_bouncyTurtle = bouncyTurtle.xcor()
            y_bouncyTurtle = bouncyTurtle.ycor()
            print(x_bouncyTurtle,y_bouncyTurtle)
            # TODO: Make sure turtle heading is set AWAY from the current boundary, otherwise it can get stuck
            if abs(x_bouncyTurtle) >= MAX_X: 
                bouncyTurtle.setheading(random.randint(90, 360))
                
            if abs(y_bouncyTurtle) >= MAX_Y:
                bouncyTurtle.setheading(random.randint(90, 360))
            bouncyTurtle.fd(1) # Moves turtle forwards 1

turtle_bounce(2) # Should only bounce turtle twice
             

winLoop = trtl.Screen()

winLoop.mainloop()
