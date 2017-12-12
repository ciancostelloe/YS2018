##Young Scientist 2018
##Author: Cian Costelloe
##PODs Game
##
##
##Initialise PODs

##ADI BLUE = 1E4056
##ADI ORANGE = FF7200
##ADI GREEN = 27B34F
##ADI PURPLE = 7C4A8B
##ADI RED = 990033
##ADI BLUE 2 = 009FBD
##ADI BLUE 3 = 3DDCE6

#############################################################

##Imports and Definitions
import serial
import time
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
   
time.sleep(6)
print('Port opened successfully\n')


######################Read Switch Values######################
print('Running switch diagnostics:')

##for i in range (0,50):
##    arduinoSerialData.write('READ_SW\r'.encode())
##    switchState = arduinoSerialData.readline();
##    time.sleep(1)
##
##    #if len(switchState) > 4:
##    #print(switchState);
##    array = list(str(switchState))
##    print(switchState)
####    for x, val in enumerate(array):
####        if array[x] == 'T':
####            print('Switch', (x - 5), 'is Low')
####        elif array[x] == 'F':
####            print('Switch ', (x - 5), 'is High')
                

######################Change Brightness values######################
##arduinoSerialData.write('SET_BRIGHTNESS:255\r'.encode())
###arduinoSerialData.write('SET_COLOUR:9:0x000000\r'.encode())
##
###Loop through each section and colour blue for 1 sec
##for colour in range (0,8):
##    arduinoSerialData.write('SET_COLOUR:%d:0x00f\r'.encode() % colour)
##    time.sleep(1)
##    arduinoSerialData.write('SET_COLOUR:%d:0x000\r'.encode() % colour)


arduinoSerialData.write('READ_SW\r'.encode())

while True:
    switchState = arduinoSerialData.readline()
    array = list(str(switchState))
    switchValues = []

    if len(array) > 8:
        for x, val in enumerate(array):
            if array[x] == 'T':
                switchValues.append(array[x])
            elif array[x] == 'F':
                switchValues.append(array[x])
        print("New values: ", switchValues)
        break

print('\nTesting complete')
























