##Main Menu


import sys
import os
from tkinter import *


def printEG():
    print("yes")


#####################GUI Setup#######################    
master = Tk()
master.title("Young Scientist 2018")
testing = Button(master, text = "Run Test", bg = "blue", fg = "white", command = runTest)
testing.pack(fill = X)

display = Button(master, text = "Display Mode", bg = "blue", fg = "white", command = printEG)
display.pack(fill = X)

game = Button(master, text = "Play Game", bg = "blue", fg = "white", command = printEG)
game.pack(fill = X)


#####################Run Test#######################
def runTest():
    os.system("python initPODs.py")
    
b = Button(master, text="Run Test", command=runTest)
b.pack(side=TOP)
mainloop()
