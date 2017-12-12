####################Display Mode###################
##Randomly change colour and randomly change POD section


import serial
import time
import random

print("Display Mode")

print('Initialising connection\n');

arduinoSerialData = serial.Serial(
  
   port='/dev/ttyUSB0',
   baudrate = 115200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
   )
   
time.sleep(6)
print('Port opened successfully\n')


def randomDisp():
    ######################Snake#############################
    red = 0xf00;
    green = 0x0f0;
    blue = 0x00f;
    lightBlue = 0x0ff;
    yellow = 0xff0;
    purple = 0xf0f;
    colourList = [red, yellow, green, lightBlue, blue, purple]

    try:
        while True:
            for colourCount, val in enumerate(colourList):
                bright = 8
                for x in range (1, 9):
                    arduinoSerialData.write('SET_BRIGHTNESS:%d\r'.encode() % bright)
                    arduinoSerialData.write('SET_COLOUR:%d:%d\r'.encode() % (x, val))
                    time.sleep(0.5)
                    bright = bright + 31
    except KeyboardInterrupt:
        print("Interrupt")
        randomDisp.quit()
        

randomDisp()
