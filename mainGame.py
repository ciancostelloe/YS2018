###############Main Game ##############################

import serial
import time
import random
import threading



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
    global  greenSec
    greenSec = random.randint(0, 7)
    print(greenSec)


##2xRed
def redNumGen1():
    global redSec1
    redSec1 = random.randint(0, 7)
    print(redSec1)
    if redSec1 == greenSec:
        print("Same Numbers: ", greenSec, redSec1)
        redNumGen1()

def redNumGen2():
    global redSec2
    redSec2 = random.randint(0, 7)
    print(redSec2, "\n")
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
    if switchValues[greenSec] == 'F':
        score = score + 1
        mainGame()
    elif switchValues[redSec1] == 'F':
        score = score - 1
        mainGame()
    elif switchValues[redSec2] == 'F':
        score = score - 1
        mainGame()
    else:
        print("Waiting for green")
        time.sleep(0.1)
        nextState()
        

##################################Game#########################################    
global score
score = 0

def mainGame():

    t0 = time.time()
    while True:
        time.sleep(0.1)

        t1 = time.time()
        if t1 - t0 < 30:
            print("Game on")
            greenNumGen()
            time.sleep(0.1)
            redNumGen1()
            time.sleep(0.1)
            redNumGen2()
            time.sleep(0.1)
            arduinoSerialData.write('SET_BRIGHTNESS:255\r'.encode())
            time.sleep(0.1)
            arduinoSerialData.write('SET_COLOUR:%d:0x0f0\r'.encode() %greenSec)
            time.sleep(0.1)
            arduinoSerialData.write('SET_COLOUR:%d:0xf00\r'.encode() %redSec1)
            time.sleep(0.1)
            arduinoSerialData.write('SET_COLOUR:%d:0xf00\r'.encode() %redSec2)

            for i in range (0,8):
                arduinoSerialData.write('READ_SW\r'.encode())
                switchState = arduinoSerialData.readline();
                time.sleep(0.01)

                if len(switchState) > 4:
                    global array
                    array = list(str(switchState))
                    global switchValues
                    switchValues = []
                    for x, val in enumerate(array):
                        if array[x] == 'T':
                            #print('Switch', (x - 5), 'is Low')
                            switchValues.append(array[x])
                        elif array[x] == 'F':
                            #print('Switch ', (x - 5), 'is High')
                            switchValues.append(array[x])
                    #print(switchValues, "\n")
                    nextState()
##              else:
##                  print("No array: ", switchState)
                        
            if score >= 0:
                print("Score = ", score)
            else:
                print("Score = 0")

            arduinoSerialData.write('SET_COLOUR:9:0x000\r'.encode())

            currTime = (t1 - t0)
            currTime = (30 - int(currTime))
            print("Time = ", currTime)
            
            
        else:
            print("Game Over")
            break


mainGame()






































