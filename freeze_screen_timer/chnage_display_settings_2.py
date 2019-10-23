# import some stuff we need
import time
from psychopy.visual import Window
from psychopy.visual import TextStim

# loop through possible screens (0 and 1 in this case)
for scr in range(0,2):
    # create a Window
    win = Window(size=(1280,1024), fullscr=True, monitor="testMonitor", units='pix', winType='pyglet', screen=scr)
    # draw some text on the Window
    TextStim(win, text="This is screen %d" %scr).draw()
    win.flip()
    # wait a bit (so you can see the Window and read the text)
    time.sleep(2)
    # close the Window again
    win.close()
    # wait a bit more before showing the next Window
    time.sleep(2)
