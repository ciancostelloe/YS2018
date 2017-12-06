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
    time.sleep(1.1)
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
    time.sleep(0.5)

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

def timer30():
    for x in range (30, 0, -1):
        time.sleep(1)
        print(x)
                
timer30()















































