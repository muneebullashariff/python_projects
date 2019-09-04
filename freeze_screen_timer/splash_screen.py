import wx
import wx.adv
import pyautogui
import logging
import time

from disable_mouse_keyboard import blockInput

## Global Variables
# Time minutes to milli-seconds
desired_minutes = 1
time_out = desired_minutes * 60 * 1000
#time_out = 5000 # 5 seconds

class MyFrame(wx.Frame):
 
    def __init__(self):

        # Getting the current screen size
        screenWidth, screenHeight = pyautogui.size()

        # Creating the Frame
        wx.Frame.__init__(self, None, wx.ID_ANY, "Tutorial", size=(screenWidth, screenHeight))
 
        bitmap = wx.Bitmap('Lion_drinking_water.png')
        splash = wx.adv.SplashScreen(
                     bitmap, 
                     wx.adv.SPLASH_CENTER_ON_SCREEN|wx.adv.SPLASH_TIMEOUT, 
                     time_out, self)
        splash.Show()
 
        self.Show()
 
 
# Run the program
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    block = blockInput()
    block.block(10)

    # Splash Image
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
   

    ### Delay between the block and unblock
    ##t0 = time.time()
    ##while time.time() - t0 < (2):
    ##    time.sleep(1)
    ##    print(time.time() - t0)

    #block.unblock()
    #logging.info("Done.")
    

