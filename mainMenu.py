##Main Menu

import sys
import os
from tkinter import *

master = Tk()

#######################Run Test#######################
def runTest():
    os.system("python initPODs.py")
    
b = Button(master, text="Run Test", command=runTest)
b.pack()
mainloop()
