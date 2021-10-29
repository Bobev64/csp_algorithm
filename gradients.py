import turtle

def gradient(t: turtle.Turtle, startingRGB: list, endingRGB: list, h: float, w: float, slope: float) -> None:
    """gradients.gradient:
        draw a single gradient with provided width and height, starting and ending at the provided colors.
    Parameters:
        - `t` (turtle.Turtle):
            the turtle used to draw the gradient
        - `startingRGB` (list):
            the RGB value to begin with
        - `endingRGB` (list):
            the RGB value to scale to
        - `h` (float):
            the height of the gradient to draw
        - `w` (float):
            the width of the gradient to draw
        - `slope` (float):
            the flope of the vertical sides of the gradient

    Notes:
        - RGB lists should be formatted like this:
            `[255, 0, 255]`
        - slope value is kind of broken"""
    
    t.pensize(1) #use the smallest availible pen size to give the gradient the highest quality
    turtle.colormode(255) #ensure the turtle is using RGB colors
    t.left(90) #turn turtle to be vertical

    for i in range(w): #each loop adds a line horizontally to the gradient
        #scale rgb values
        r = int((endingRGB[0]-startingRGB[0])*(i/w) + startingRGB[0])
        g = int((endingRGB[1]-startingRGB[1])*(i/w) + startingRGB[1])
        b = int((endingRGB[2]-startingRGB[2])*(i/w) + startingRGB[2])

        #set turtle to have the calculated colors
        t.color((r, g, b))

        #swap between moving forward and backward each loop, kind of like a scanner
        t.forward(h) if i%2 == 0 else t.backward(h)
        #move a bit right after drawing a line
        t.goto(t.xcor()+1, t.ycor() + slope)

def doubleGradient(t: turtle.Turtle, startingRGB: list, middleRGB: list, endingRGB: list, h: float, w: float, slope: float) -> None:
    """gradients.gradient:
        draw a double gradient with provided width and height, scaling from the starting value to the middle, and the middle to the end.
    Parameters:
        - `t` (turtle.Turtle):
            the turtle used to draw the gradient
        - `startingRGB` (list):
            the RGB value to begin with
        - `startingRGB` (list):
            the RGB value to scale to in the middle
        - `endingRGB` (list):
            the RGB value to scale to after the middle
        - `h` (float):
            the height of the gradient to draw
        - `w` (float):
            the width of the gradient to draw
        - `slope` (float):
            the flope of the vertical sides of the gradient

    Notes:
        - RGB lists should be formatted like this:
            `[255, 0, 255]`
        - slope value is kind of broken"""
    #call the gradient function twice
    gradient(t, startingRGB, middleRGB, h, int(w/2), slope)
    t.right(90) #reset position after running
    gradient(t, middleRGB, endingRGB, h, int(w/2), slope)

def multiGradient(t: turtle.Turtle, RGB: list, h: float, w: float, slope: float) -> None:
    """gradients.gradient:
        draw any amount of gradients with provided dimensions.
    Parameters:
        - `t` (turtle.Turtle):
            the turtle used to draw the gradient
        - `RGB` (list):
            a list containing multiple RGB colors to scale between
        - `h` (float):
            the height of the gradient to draw
        - `w` (float):
            the width of the gradient to draw
        - `slope` (float):
            the flope of the vertical sides of the gradient

    Notes:
        - RGB list should be formatted like this: [[0, 0, 0], [255, 255, 255]]
        - RGB color lists should be formatted like this:
            `[255, 0, 255]`
        - slope value is kind of broken"""
    for i in range(len(RGB)-1): #loop once for each gradient range provided
        gradient(t, RGB[i], RGB[i+1], h, int(w/(len(RGB)-1)), slope) #draw a gradient with each gradient range provided
        t.right(90) #reset position after drawing