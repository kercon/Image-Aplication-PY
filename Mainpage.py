import sys
sys.path.append("D:\Workspaces PY\Image Aplication\PYLIB")
from appJar import gui

# create the GUI & set a title
app = gui("Login Form")
# add labels & entries
# in the correct row & column
app.addLabel("userLab", "Username:", 0, 0)
app.addEntry("userEnt", 0, 1)
app.addLabel("passLab", "Password:", 1, 0)
app.addEntry("passEnt", 1, 1)

# start the GUI
app.go()