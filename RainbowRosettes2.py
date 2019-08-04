# RainbowRosettes2.py
# Billy Ridgeway
# Creates a rainbow rosette where the user can select the number of circles.

import turtle           # Imports the turtle library.
import colorsys         # Imports the colorsys library.
t = turtle.Pen()        # Creates a new turtle pen.
t.shape("turtle")       # Makes the pen look like a turtle.
turtle.bgcolor('black') # Sets the background color to black.
t.speed(0)              # Sets the pen's speed to fast.
t.width(3)              # Sets the pen's width to 3 pixels.

# Asks the user for the number of circles in their rosette, default to 26
number_of_circles = int(turtle.numinput("Number of circles",
                                        "How many circles do you want in your rosette? ", 26))

for n in range(number_of_circles):                              # Sets n to the number of circles selected by the user.
    t.pencolor(colorsys.hsv_to_rgb(n/number_of_circles,1,1) )   # Cycles through colors.
    t.circle(150)                                               # Sets the size of the circle.
    t.left(360/number_of_circles)                               # Moves the pen left by 360 divided by the number of circles
                                                                # Selected by the user.

