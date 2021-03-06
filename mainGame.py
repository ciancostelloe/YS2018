###############Main Game ##############################
import serial
import time
import random
import threading
import sys

global score1
score1 = 0
global score2
score2 = 0


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

##USB2
##arduinoSerialData2 = serial.Serial(
##  
##   port='/dev/ttyUSB1',
##   baudrate = 115200,
##   parity=serial.PARITY_NONE,
##   stopbits=serial.STOPBITS_ONE,
##   bytesize=serial.EIGHTBITS,
##   timeout=1
##   )

time.sleep(8)
arduinoSerialData.flushInput()
print('Port opened successfully\n')


####################Define Colours############################
red = 0xf00;
green = 0x0f0;
blue = 0x00f;
lightBlue = 0x0ff;
yellow = 0xff0;
purple = 0xf0f;
colourList = [red, yellow, green, lightBlue, blue, purple]

####################3 - 2 - 1#################################
def trafficLight():
    
    arduinoSerialData.write('SET_BRIGHTNESS:255\r'.encode())
    arduinoSerialData.write('SET_COLOUR:9:0xf00\r'.encode())
    time.sleep(1.2)
    arduinoSerialData.write('SET_COLOUR:9:0x000\r'.encode())
    time.sleep(0.5)

    arduinoSerialData.write('SET_BRIGHTNESS:255\r'.encode())
    arduinoSerialData.write('SET_COLOUR:9:0xff0\r'.encode())
    time.sleep(1)
    arduinoSerialData.write('SET_COLOUR:9:0x000\r'.encode())
    time.sleep(0.4)
    
    arduinoSerialData.write('SET_BRIGHTNESS:255\r'.encode())
    arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
    time.sleep(0.8)
    arduinoSerialData.write('SET_COLOUR:9:0x000\r'.encode())
    time.sleep(0.1)

#trafficLight()

#####################Random Generator POD 1#######################################

##Green
def greenNumGen():
    global greenSec
    greenSec = random.randint(1, 8)
    print(greenSec)


##2xRed
def redNumGen1():
    global redSec1
    redSec1 = random.randint(1, 8)
    print(redSec1)
    if redSec1 == greenSec:
        print("Same Numbers: ", greenSec, redSec1)
        redNumGen1()

def redNumGen2():
    global redSec2
    redSec2 = random.randint(1, 8)
    print(redSec2)
    if (redSec2 == redSec1):
        print("Same reds: ",greenSec, redSec1, redSec2)
        redNumGen2()
    elif (redSec2 == greenSec):
        print("Same as green: ", greenSec, redSec1, redSec2)
        redNumGen2()
        


###############################30 second timer###################################

##def timer30():
##    global timer
##    for timer in range (30, 0, -1):
##        time.sleep(1)
##        #print(timer)
##        if timer == 1:
##            time.sleep(1)
##            print("Game Over")
###timer30()


################################States#########################################

def nextState():
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

    testArray = ['T', 'F', 'T', 'F', 'T', 'F', 'T', 'F', 'T']
    #time.sleep(2)

    
    while True:
        t1 = time.time()
        if t1 - t0 < 30:
            currTime = (t1 - t0)
            currTime = (30 - int(currTime))
            print("Time2 = ", currTime)

            
            switchState = arduinoSerialData.readline()
            array = list(str(switchState))
            switchValues = []

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

        else:
            print("Game Over")
            if score1 > score2:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            elif score1 == score2:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            else:
                arduinoSerialData.write('SET_COLOUR:9:0xf00\r'.encode())

##            if score2 > score1:
##                arduinoSerialData2.write('SET_COLOUR:9:0x0f0\r'.encode())
##            elif score2 == score1:
##                arduinoSerialData2.write('SET_COLOUR:9:0x0f0\r'.encode())
##            else:
##                arduinoSerialData2.write('SET_COLOUR:9:0xf00\r'.encode())
            time.sleep(1)
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
    score = 0

    
    while True:
        t1 = time.time()
        if t1 - t0 < 30:
            print("\nGame on")
            currTime = (t1 - t0)
            currTime = (30 - int(currTime))
            print("Time1 = ", currTime)
            greenNumGen()
            time.sleep(0.01)
            redNumGen1()
            time.sleep(0.01)
            redNumGen2()
            time.sleep(0.01)
            arduinoSerialData.write('SET_BRIGHTNESS:255\r'.encode())
            time.sleep(0.01)
            arduinoSerialData.write('SET_COLOUR:%d:0x0f0\r'.encode() %greenSec)
            time.sleep(0.01)
            arduinoSerialData.write('SET_COLOUR:%d:0xf00\r'.encode() %redSec1)
            time.sleep(0.01)
            arduinoSerialData.write('SET_COLOUR:%d:0xf00\r'.encode() %redSec2)
            time.sleep(0.25)

            arduinoSerialData.write('READ_SW\r'.encode())
            time.sleep(0.01)
            nextState()
            
            if score1 > 0:
                print("Score = ", score1)
            else:
                print("Score = 0")
            #time.sleep(4)
            arduinoSerialData.write('SET_COLOUR:9:0x000\r'.encode())

            time.sleep(0.01)
        else:
            print("Game Over")
            if score1 > score2:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            elif score2 > score1:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            elif score2 == score1:
                arduinoSerialData.write('SET_COLOUR:9:0x0f0\r'.encode())
            else:
                arduinoSerialData.write('SET_COLOUR:9:0xf00\r'.encode())
            break


t0 = time.time()

mainGame()






































