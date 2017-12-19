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
logoArray = [PhotoImage(file= imageArray[0]), PhotoImage(file= imageArray[1]), PhotoImage(file= imageArray[2]), PhotoImage(file= imageArray[3]), PhotoImage(file= imageArray[4]), PhotoImage(file= imageArray[5]), PhotoImage(file= imageArray[6]), PhotoImage(file= imageArray[7])]



randy = random.randint(0, 7)
logo1 = logoArray[randy]
w1 = Label(root, image=logo1).place(x = 200, y = 400, anchor = "center")
logo2 = logoArray[randy]
w2 = Label(root, image=logo2).place(x = 600, y = 400, anchor = "center")


var = StringVar()
var.set('Player 1')
l = Entry(fr, textvariable = var, bg = "white", font=("Courier", 22))
l.place(x = 25, y = 25, anchor = "w")

var2 = StringVar()
var2.set('Player 2')
l2 = Entry(fr, textvariable = var2, bg = "white", font=("Courier", 22))
l2.place(x = 775, y = 25, anchor = "e")

var3 = StringVar()
var3.set('Time')
l3 = Label(fr, textvariable = var3, bg = "white", font=("Courier", 22))
l3.place(x = 395, y = 80, anchor = "center")

var4 = StringVar()
var4.set('Score')
l4 = Label(fr, textvariable = var4, bg = "white", font=("Courier", 18))
l4.place(x = 25, y = 75, anchor = "w")
podScore1 = StringVar()
podScore1.set('0')
scoreLabel1 = Label(fr, textvariable = podScore1, bg = "white", font=("Helvetica", 26))
scoreLabel1.place(x = 25, y = 115, anchor = "w")


timeVar = StringVar()
x = 30
timeVar.set(x)
l6 = Label(fr, textvariable = timeVar, bg = "white", font=("Helvetica", 18))
l6.place(x = 395, y = 120, anchor = "center")

var5 = StringVar()
var5.set('Score')
l5 = Label(fr, textvariable = var5, bg = "white", font=("Courier", 18))
l5.place(x = 775, y = 75, anchor = "e")
podScore2 = StringVar()
podScore2.set('0')
scoreLabel2 = Label(fr, textvariable = podScore1, bg = "white", font=("Helvetica", 26))
scoreLabel2.place(x = 775, y = 115, anchor = "e")

time.sleep(1)
root.update()











root.mainloop() # the window is now displayed
