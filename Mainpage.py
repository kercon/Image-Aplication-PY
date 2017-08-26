import sys
from appJar import gui
from toolbar import *


def toolbar(btn):
    print(btn)
    if btn == "EXIT":
        app.stop()
    elif btn == "FULL-SCREEN":
        if app.exitFullscreen():
            app.setToolbarIcon("FULL-SCREEN", "FULL-SCREEN")
        else:
            app.setGeometry("fullscreen")
            app.setToolbarIcon("FULL-SCREEN", "FULL-SCREEN-EXIT")

# create the GUI & set a title
app = gui("Login Form")
# add file menu options
app.addMenuPreferences(toolbar)
app.addMenuItem(
    "Main", "EXIT", toolbar, shortcut="Control-B",
    underline=2)
app.addMenuItem("Screen", "FULL-SCREEN", toolbar)
# start the GUI
app.go()
