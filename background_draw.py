import turtle as trtl

screenSize = (trtl.screensize()) # Screen width first tuple, second height

drawer = trtl.Turtle()

drawer.setheading(135)
drawer.forward(20)



def bottom_draw(window_width):

    numOfLines = window_width / 12
    


winLoop = trtl.Screen()
winLoop.mainloop()

# Draw line in the middle of screen, draw diagonal to meet that line based on pythagorean theorem
# rest of lines will match with diagonal lines on bottom and meet with this center line