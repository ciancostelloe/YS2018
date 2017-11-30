##Young Scientist 2018
##Author: Cian Costelloe
##PODs Game
##
##
##Initialise PODs

#############################################################

##Imports and Definitions
import serial
import time
#from Tkinter import *

print('Initialising connection');

arduinoSerialData = serial.Serial(
  
   port='/dev/ttyUSB0',
   baudrate = 115200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
   )
   
time.sleep(6)
print('Port opened successfully')

######################Read Switch Values######################
print('Running switch diagnostics')

for i in range (0,4):
    arduinoSerialData.write('READ_SW\r'.encode())
    switchState = arduinoSerialData.readline();
    time.sleep(0.1)

    if len(switchState) > 4:
        print(switchState);
        array = list(str(switchState))
        print(array)
        for x, val in enumerate(array):
            if array[x] == 'T':
                print('Switch', x, 'is Low')
            elif array[x] == 'F':
                print('Switch ', x, 'is High')
                

######################Read Switch Values######################

arduinoSerialData.write('SET_COLOUR:9:0xfff\r'.encode())
