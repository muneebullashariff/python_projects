import turtle
import time
import pyautogui

# Getting the current screen size
screenWidth, screenHeight = pyautogui.size()

screen = turtle.Screen()
#screen.setup(600,400)
screen.setup(screenWidth, screenHeight)
screen.bgpic('Lion_drinking_water.gif')
screen.update()

#screen.bgpic('image2.gif')

# Used so that the window doesn't get closed
screen.mainloop()

