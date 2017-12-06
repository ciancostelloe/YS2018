##Main Menu


import sys
import os
from tkinter import *


def printEG():
    print("yes")

#####################Run Test#######################
def runTest():
    os.system("python initPODs.py")

#####################Display Mode#######################
def dispMode():
    os.system("python displayMode.py")

#####################Quit#############################
def quit(event):
    print ("You pressed Ctrl-C")
    master.quit()

#####################GUI Setup#######################    
master = Tk()
master.title("Young Scientist 2018")
testing = Button(master, text = "Run Test", bg = "blue", fg = "white", command = runTest)
testing.pack(fill = X)

display = Button(master, text = "Display Mode", bg = "blue", fg = "white", command = dispMode)
display.pack(fill = X)

game = Button(master, text = "Play Game", bg = "blue", fg = "white", command = printEG)
game.pack(fill = X)

master.bind('<Control-c>', quit)
mainloop()
