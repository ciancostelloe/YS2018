from tkinter import *
import os
import time
import random

root = Tk()
ADI = '#1E4056'
fr = Frame(root, bg = ADI, width = 800, height = 600)
root.title("Young Scientist 2018")
fr.grid(row = 0, column = 0)
fr.grid_propagate(0)
fr.update()

imageArray = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png"]


logo1 = PhotoImage(file= "1.png")
w1 = Label(root, image=logo1).place(x = 200, y = 400, anchor = "center")
logo2 = PhotoImage(file= "3.png")
w2 = Label(root, image=logo2).place(x = 600, y = 400, anchor = "center")


var = StringVar()
var.set('Player 1')
var2 = StringVar()
var2.set('Player 2')
var3 = StringVar()
var3.set('Time')
var4 = StringVar()
var4.set('Score')
timeVar = StringVar()
timeVar.set('30')
var5 = StringVar()
var5.set('Score')


l = Entry(fr, textvariable = var, bg = "white", font=("Courier", 22))
l.place(x = 25, y = 25, anchor = "w")

l3 = Label(fr, textvariable = var3, bg = "white", font=("Courier", 22))
l3.place(x = 395, y = 80, anchor = "center")

l6 = Label(fr, textvariable = timeVar, bg = "white", font=("Courier", 18))
l6.place(x = 395, y = 120, anchor = "center")

l2 = Entry(fr, textvariable = var2, bg = "white", font=("Courier", 22))
l2.place(x = 775, y = 25, anchor = "e")

l4 = Label(fr, textvariable = var4, bg = "white", font=("Courier", 18))
l4.place(x = 25, y = 75, anchor = "w")

l5 = Label(fr, textvariable = var5, bg = "white", font=("Courier", 18))
l5.place(x = 775, y = 75, anchor = "e")




root.mainloop() # the window is now displayed
