from win32api import GetSystemMetrics
import win32gui
import win32con 

window = win32gui.GetForegroundWindow() # retrieves the freshly opened window
win32gui.MoveWindow(window, GetSystemMetrics(0), 0, 0, 0, True) # translates it about the main monitor width
win32gui.ShowWindow(window, win32con.SW_MAXIMIZE) # maximizes the window
