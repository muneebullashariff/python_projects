## Used for time difference between start and end
#from datetime import datetime as dt
#starttime = dt.now()
#input("Mark end time")
#endtime = dt.now()
#print("Total time passed is {}.".format(endtime-starttime))

## Used for locking the screen
#import ctypes
#print("Executing the lock")
#ctypes.windll.user32.LockWorkStation()
#print("After the lock")

## Moving the mouse to the middle of the screen
#import pyautogui
#screenWidth, screenHeight = pyautogui.size()
#pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

## To type the string without the keyboard
#import pyautogui
#pyautogui.typewrite('Hello world!')      

# Message box functions
import pyautogui
# 1 - alert function
pyautogui.PAUSE=5
pyautogui.alert(text='Meal 1', title='Food Schedule', button='OK')
pyautogui.alert(text='Drink water', title='Food Schedule', button='OK')
