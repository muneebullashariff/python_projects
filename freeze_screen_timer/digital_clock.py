import turtle
import time
import pyautogui
import threading
import logging
import ctypes

from disable_mouse_keyboard import blockInput

# Getting the current screen size
screenWidth, screenHeight = pyautogui.size()

# Turtle Screen
screen = turtle.Screen()
screen1plus2Width = 2710
screen.setup(screen1plus2Width, screenHeight,0,0) # Start at left most x,y = 0,0
#screen.setup(screenWidth, screenHeight)

#screen.bgpic('Lion_drinking_water.gif')
screen.bgpic('Lion_drinking_water_1366_768.gif')

screen.update()

class Timer(turtle.Turtle):
    def __init__(self, x, y, c, p, sec):
        turtle.Turtle.__init__(self)
        self.sec = sec
        self.pensize = p
        #self.action = action

        #self.x = x
        #self.y = y 

        self.ht()
        self.color(c)
        self.penup()
        self.goto(x,y)
        #self.write(time.strftime("%H:%M:%S",time.gmtime(self.sec)), False
        #            , align="right", font=("Arial", self.pensize, "bold"))

    def start(self):
        self.clear()

        #self.goto(self.x, self.y)
        self.write(time.strftime("%H:%M:%S",time.gmtime(self.sec)), False
                    , align="right", font=("Arial", self.pensize, "bold"))

        self.sec -= 1
        if self.sec != -1:
            screen.ontimer(self.start, 1000) # 1000 milliseconds = 1 second
        else:
            # Lock the screen after the thread is done
            ctypes.windll.user32.LockWorkStation()
            quit()
    
minutes = 1
seconds = minutes*60
seconds = 10 # For testing

#timer = Timer(0, -100, "red", 100, seconds)#), testaction)
#timer = Timer(300, -200, "red", 90, seconds)#), testaction)

logging.basicConfig(level=logging.INFO)
block = blockInput()
block.block(seconds)

# minus 3 seconds because the threading is taking some time
timer = Timer(-200, 200, "red", 90, seconds-3)#), testaction)
timer2 = Timer(-200+screenWidth, 200, "red", 90, seconds-3)#), testaction)

t1 = threading.Thread(target=timer.start)
t2 = threading.Thread(target=timer2.start)

t1.start()
t2.start()

#t1.join()
#t2.join()

# Used so that the window doesn't get closed
screen.mainloop()

