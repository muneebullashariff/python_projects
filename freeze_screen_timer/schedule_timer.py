import turtle
import time
import pyautogui
from digital_clock import Timer

# Getting the current screen size
screenWidth, screenHeight = pyautogui.size()

# Turtle Screen
screen = turtle.Screen()
screen.setup(screenWidth, screenHeight)
screen.bgpic('Lion_drinking_water.gif')
screen.title("Muneeb Work Schedule")
screen.update()

## Create our drawing pen
pen = turtle.Turtle()
# Hides the pen on the screen but we can draw using it
pen.hideturtle()
# It'll draw as fast as it can
pen.speed(0)
# Width of the lines drawn
pen.pensize(3)



# Used so that the window doesn't get closed
screen.mainloop()
