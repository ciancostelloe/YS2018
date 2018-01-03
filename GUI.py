#######################Imports###############################
from tkinter import *
import os
import time
import random
import sys
import serial
import threading

##########################Stats##############################
##statsFile = open("stats.txt", "w")
##statsFile.write("Count: 0")
##statsFile.close()

statsFile = open("stats.txt", "r")
stats = statsFile.readline().replace('Count:', ' ')

stats = int(stats) + 1
print(stats)

statsFile = open("stats.txt", "w")
statsFile.write("Count: %d" %stats)


#####################Globals###############################
global score1
global score2
global lastGreen
global lastRed
global lastRed2
global lastGreenP2
global lastRedP2
global lastRed2P2

score1 = 0
score2 = 0
lastGreen = 0
lastRed = 0
lastRed2 = 0
lastGreenP2 = 0
lastRedP2 = 0
lastRed2P2 = 0


########################Definitions############################
def stopGame():
    print("Game Ended")
    sys.exit()

    
#########################Frame##################################
root = Tk()
ADI = '#1E4056'
fr = Frame(root, bg = ADI, width = 800, height = 600)
root.title("Young Scientist 2018")
fr.grid(row = 0, column = 0)
fr.grid_propagate(0)
fr.update()

gameCount = StringVar()
gameCount.set('Games played: %d' %stats)
countBox = Label(fr, textvariable = gameCount,fg = "white", bg = ADI, font=("Courier", 12))
countBox.place(x = 10, y = 580, anchor = "w")

#########################Load images###########################
imageArray = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png"]
logoArray = [PhotoImage(file= imageArray[0]), PhotoImage(file= imageArray[1]), PhotoImage(file= imageArray[2]), PhotoImage(file= imageArray[3]), PhotoImage(file= imageArray[4]), PhotoImage(file= imageArray[5]), PhotoImage(file= imageArray[6]), PhotoImage(file= imageArray[7])]


##############################################################################################
##########################################Main################################################
##############################################################################################

def startGame():
    global score1
    global score2
    global switchValues
    global swithState
    global array
    global greenSec
    global redSec1
    global redSec2
    global t1
    global t0
    global arduinoSerialData
    global arduinoSerialData2
    print("Game started")
    print('Initialising connection\n');

    ##USB1
    arduinoSerialData = serial.Serial(
       port='/dev/ttyUSB0',
       baudrate = 115200,
       parity=serial.PARITY_NONE,
       stopbits=serial.STOPBITS_ONE,
       bytesize=serial.EIGHTBITS,
       timeout=1
       )

##    ##USB2
##    arduinoSerialData2 = serial.Serial(
##       port='/dev/ttyUSB1',
##       baudrate = 115200,
##       parity=serial.PARITY_NONE,
##       stopbits=serial.STOPBITS_ONE,
##       bytesize=serial.EIGHTBITS,
##       timeout=1
##       )
    
    time.sleep(8)
    arduinoSerialData.flushInput()
    #arduinoSerialData2.flushInput()
    print('Ports opened successfully\n')


    ####################Define Colours############################
    red = 0xf00;
    green = 0x0f0;
    blue = 0x00f;
    lightBlue = 0x0ff;
    yellow = 0xff0;
    purple = 0xf0f;
    colourList = [red, yellow, green, lightBlue, blue, purple]

    t0 = time.time()
    mainGame()

#####################Random Generator POD 1#######################################

##Green
def greenNumGen():
    global greenSec
    global lastGreen
    greenSec = random.randint(1, 8)
    print(greenSec)
    if greenSec == lastGreen:
        greenNumGen()
    lastGreen = greenSec


##2xRed
def redNumGen1():
    global redSec1
    global lastRed
    redSec1 = random.randint(1, 8)
    print(redSec1)
    if redSec1 == greenSec:
        print("Same Numbers: ", greenSec, redSec1)
        redNumGen1()
    elif redSec1 == lastRed:
        redNumGen1()
    lastRed = redSec1

def redNumGen2():
    global redSec2
    global lastRed2
    redSec2 = random.randint(1, 8)
    print(redSec2)
    if (redSec2 == redSec1):
        print("Same reds: ",greenSec, redSec1, redSec2)
        redNumGen2()
    elif (redSec2 == greenSec):
        print("Same as green: ", greenSec, redSec1, redSec2)
        redNumGen2()
    elif redSec2 == lastRed2:
        redNumGen2()
    lastRed2 = redSec2


#####################Random Generator POD 2#######################################

##Green
def greenNumGenP2():
    global greenSecP2
    global lastGreenP2
    greenSecP2 = random.randint(1, 8)
    print(greenSecP2)
    if greenSecP2 == lastGreenP2:
        greenNumGenP2()
    lastGreenP2 = greenSecP2


##2xRed
def redNumGen1P2():
    global redSec1P2
    global lastRedP2
    redSec1P2 = random.randint(1, 8)
    print(redSec1P2)
    if redSec1P2 == greenSecP2:
        print("Same Numbers: ", greenSecP2, redNumGen1P2)
        redNumGen1P2()
    elif redSec1P2 == lastRedP2:
        redNumGen()
    lastRedP2 = redSec1P2

def redNumGen2P2():
    global redSec2P2
    global lastRed2P2
    redSec2P2 = random.randint(1, 8)
    print(redSec2P2)
    if (redSec2P2 == redSec1P2):
        print("Same reds: ",greenSecP2, redSec1P2, redSec2P2)
        redNumGen2P2()
    elif (redSec2P2 == greenSecP2):
        print("Same as green: ", greenSecP2, redSec1P2, redSec2)
        redNumGen2P2()
    elif redSec2P2 == lastRed2P2:
        redNumGen2P2()
    lastRed2P2 = redSec2P2
    

################################States#########################################

def nextState():
    global score1
    global score2
    global switchValues
    global switchValues2
    global swithState
    global switchState2
    global array
    global array2
    global greenSec
    global redSec1
    global redSec2
    global greenSecP2
    global redSec1P2
    global redSec2P2
    global arduinoSerialData
    global arduinoSerialData2
    global t1
    global t0
    global podScore1

    #testArray = ['T', 'F', 'T', 'F', 'T', 'F', 'T', 'F', 'T']
    #time.sleep(2)

    while True:
        t1 = time.time()
        if t1 - t0 < 30:
            currTime = (t1 - t0)
            currTime = (30 - int(currTime))
            print("Time = ", currTime)
            
            timeVar = StringVar()
            timeVar.set(currTime)
            l6 = Label(fr, textvariable = timeVar, bg = "white", font=("Helvetica", 18))
            l6.place(x = 395, y = 120, anchor = "center")

            switchState = arduinoSerialData.readline()
            array = list(str(switchState))
            switchValues = []

##            switchState2 = arduinoSerialData2.readline()
##            array2 = list(str(switchState2))
##            switchValues2 = []

            if len(array) > 8:
                for x, val in enumerate(array):
                    if array[x] == 'T':
                        switchValues.insert(0, array[x])
                    elif array[x] == 'F':
                        switchValues.insert(0, array[x])
                print("Switch values: ", switchValues)
        
                if switchValues[greenSec] == 'F':
                    score1 = score1 + 1
                    return 0
                elif switchValues[redSec1] == 'F':
                    if score1 == 0:
                        return 0
                    else:
                        score1 = score1 - 1
                        return 0
                elif switchValues[redSec2] == 'F':
                    if score1 == 0:
                        return 0
                    else:
                        score1 = score1 - 1
                    return 0
                else:
                    print("Hit the green tile!")
                    arduinoSerialData.write('READ_SW\r'.encode())
                    time.sleep(0.1)
                    continue
            
            podScore1 = StringVar()
            podScore1.set(score1)
            scoreLabel1 = Label(fr, textvariable = podScore1, bg = "white", font=("Helvetica", 26))
            scoreLabel1.place(x = 25, y = 115, anchor = "w")
            root.update()

            
##            if len(array2) > 8:
##                for x, val in enumerate(array2):
##                    if array2[x] == 'T':
##                        switchValues2.append(array2[x])
##                    elif array2[x] == 'F':
##                        switchValues2.append(array2[x])
##                print("Switch values: ", switchValues2)
##        
##                if switchValues2[greenSecP2 - 1] == 'F':
##                    score2 = score2 + 1
##                    return 0
##                elif switchValues2[redSec1P2 - 1] == 'F':
##                    if score2 == 0:
##                        return 0
##                    else:
##                        score2 = score2 - 1
##                        return 0
##                elif switchValues2[redSec2P2 - 1] == 'F':
##                    if score2 == 0:
##                        return 0
##                    else:
##                        score2 = score2 - 1
##                    return 0
##                else:
##                    print("Hit the green tile!")
##                    arduinoSerialData2.write('READ_SW\r'.encode())
##                    time.sleep(0.1)
##                    continue

##            podScore2 = StringVar()
##            podScore2.set(score2)
##            scoreLabel2 = Label(fr, textvariable = podScore2, bg = "white", font=("Helvetica", 26))
##            scoreLabel2.place(x = 775, y = 115, anchor = "e")
##            root.update()

        else:
            name1 = l.get()
            name2 = l2.get()
            statsFile.write("\n%s %s" %(name1, score1))
            statsFile.write("\n%s %s" %(name2, score2))
            statsFile.close()
            print("Game Over")
            if score1 > score2:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            elif score1 == score2:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            else:
                arduinoSerialData.write('SET_COLOUR:9:0xf00\r'.encode())

            if score2 > score1:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            elif score2 == score1:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            else:
                arduinoSerialData.write('SET_COLOUR:9:0xf00\r'.encode())
            time.sleep(2)
            arduinoSerialData.write('SET_COLOUR:9:0x000\r'.encode())
            sys.exit()
        

##################################Game#########################################    

def mainGame():
    global score1
    global score2
    global switchValues
    global array
    global t0
    global t1
    global switchState
    global arduinoSerialData
    global currTime
    global podScore1
    score = 0

    
    while True:
        t1 = time.time()
        if t1 - t0 < 30:
            print("\nGame on")
            currTime = (t1 - t0)
            currTime = (30 - int(currTime))
            print("Time = ", currTime)
            greenNumGen()
            redNumGen1()
            redNumGen2()
            greenNumGenP2()
            redNumGen1P2()
            redNumGen2P2()            
            arduinoSerialData.write('SET_BRIGHTNESS:255\r'.encode())
            time.sleep(0.01)
            arduinoSerialData.write('SET_COLOUR:%d:0x0f0\r'.encode() %greenSec)
            time.sleep(0.01)
            arduinoSerialData.write('SET_COLOUR:%d:0xf00\r'.encode() %redSec1)
            time.sleep(0.01)
            arduinoSerialData.write('SET_COLOUR:%d:0xf00\r'.encode() %redSec2)
##            time.sleep(0.01)
##            arduinoSerialData2.write('SET_COLOUR:%d:0x0f0\r'.encode() %greenSecP2)
##            time.sleep(0.01)
##            arduinoSerialData2.write('SET_COLOUR:%d:0xf00\r'.encode() %redSec1P2)
##            time.sleep(0.01)
##            arduinoSerialData2.write('SET_COLOUR:%d:0xf00\r'.encode() %redSec2P2)
            time.sleep(0.25)

            arduinoSerialData.write('READ_SW\r'.encode())
            time.sleep(0.01)
            nextState()
            
            if score1 > 0:
                print("Score = ", score)
            else:
                print("Score = 0")
            #time.sleep(4)
            arduinoSerialData.write('SET_COLOUR:9:0x000\r'.encode())
            time.sleep(0.1)
        else:
            print("Game Over")
            if score1 > score2:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            elif score1 == score2:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            else:
                arduinoSerialData.write('SET_COLOUR:9:0xf00\r'.encode())

            if score2 > score1:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            elif score2 == score1:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            else:
                arduinoSerialData.write('SET_COLOUR:9:0xf00\r'.encode())
            break
        


randy = random.randint(0, 7)
logo1 = logoArray[randy]
w1 = Label(root, image=logo1).place(x = 200, y = 400, anchor = "center")
logo2 = logoArray[randy]
w2 = Label(root, image=logo2).place(x = 600, y = 400, anchor = "center")


#####################Create and set labels###############################
player1Name = StringVar()
player1Name.set('Player 1')
l = Entry(fr, textvariable = player1Name, bg = "white", font=("Courier", 22))
l.place(x = 25, y = 25, anchor = "w")

player2Name = StringVar()
player2Name.set('Player 2')
l2 = Entry(fr, textvariable = player2Name, bg = "white", font=("Courier", 22))
l2.place(x = 775, y = 25, anchor = "e")

var3 = StringVar()
var3.set('Time')
l3 = Label(fr, textvariable = var3, bg = "white", font=("Courier", 22))
l3.place(x = 395, y = 80, anchor = "center")

score1Var = StringVar()
score1Var.set('Score')
l4 = Label(fr, textvariable = score1Var, bg = "white", font=("Courier", 18))
l4.place(x = 25, y = 75, anchor = "w")

##podScore1 = StringVar()
##podScore1.set('0')
##scoreLabel1 = Label(fr, textvariable = podScore1, bg = "white", font=("Helvetica", 26))
##scoreLabel1.place(x = 25, y = 115, anchor = "w")

##timeVar = StringVar()
##currTime = 30
##timeVar.set(currTime)
##l6 = Label(fr, textvariable = timeVar, bg = "white", font=("Helvetica", 18))
##l6.place(x = 395, y = 120, anchor = "center")

startButton = Button(fr, bg = ADI, fg = "white", text ="Start", command = startGame)
startButton.place(x = 365, y = 170, anchor = "center")

stopButton = Button(fr, bg = ADI, fg = "white", text ="Stop", command = stopGame)
stopButton.place(x = 425, y = 170, anchor = "center")


score2Var = StringVar()
score2Var.set('Score')
l5 = Label(fr, textvariable = score2Var, bg = "white", font=("Courier", 18))
l5.place(x = 775, y = 75, anchor = "e")


##podScore2 = StringVar()
##podScore2.set('0')
##scoreLabel2 = Label(fr, textvariable = podScore2, bg = "white", font=("Helvetica", 26))
##scoreLabel2.place(x = 775, y = 115, anchor = "e")

root.update()

root.mainloop()












































































