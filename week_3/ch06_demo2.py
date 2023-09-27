# Topic : turtle , random Modules
# DEMO

import turtle
import random

turtle.shape("turtle")

# turtle.speed(1)
# turtle.color(1, 0, 1)  # Red Green Blue
# turtle.forward(100) # 100 pixel
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.done()


def drawCircle(x, y):
    # Draw a circle there , and fill it with a random color .
    turtle.fillcolor(random.random(), random.random(), random.random())  #RGB
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.up()
#
turtle.title ("Click on the canvas !")
#
# bind left mouse button to drawCircle function
turtle.onscreenclick(drawCircle)

# Initiate main loop
turtle.mainloop()




# spaceship game
# http://www.codeskulptor.org/#user43_7zb1ohzfMl_35.py
