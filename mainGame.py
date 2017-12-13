###############Main Game ##############################

import serial
import time
import random
import threading
import sys


print('Initialising connection\n');

arduinoSerialData = serial.Serial(
  
   port='/dev/ttyUSB0',
   baudrate = 115200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
   )
   
time.sleep(5)
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
        

#greenNumGen()
#redNumGen1()
#redNumGen2()
#print("Final values = ", greenSec, redSec1, redSec2)


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
    global score
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
            print("Time = ", currTime)
            switchState = arduinoSerialData.readline()
            array = list(str(switchState))
            switchValues = []

            if len(array) > 8:
                for x, val in enumerate(array):
                    if array[x] == 'T':
                        switchValues.append(array[x])
                    elif array[x] == 'F':
                        switchValues.append(array[x])
                print("Switch values: ", switchValues)
        
                if testArray[greenSec - 1] == 'F':
                    score = score + 1
                    return 0
                elif testArray[redSec1 - 1] == 'F':
                    if score == 0:
                        return 0
                    else:
                        score = score - 1
                        return 0
                elif testArray[redSec2 - 1] == 'F':
                    if score == 0:
                        return 0
                    else:
                        score = score - 1
                    return 0
                else:
                    print("Hit the green tile!")
                    arduinoSerialData.write('READ_SW\r'.encode())
                    time.sleep(0.1)
                    continue
        else:
            print("Game Over")
            sys.exit()
        
##        nextState()
        

##################################Game#########################################    

def mainGame():
    global score
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
            print("Time = ", currTime)
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
            time.sleep(0.3)

            arduinoSerialData.write('READ_SW\r'.encode())

            nextState()
            
            if score > 0:
                print("Score = ", score)
            else:
                print("Score = 0")
            #time.sleep(4)
            arduinoSerialData.write('SET_COLOUR:9:0x000\r'.encode())
            time.sleep(0.1)
        else:
            print("Game Over")
            break

t0 = time.time()

mainGame()






































