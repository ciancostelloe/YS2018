import serial
import time
import random
import threading
import sys

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

time.sleep(8)
arduinoSerialData.flushInput()
print('Port opened successfully\n')

arduinoSerialData.write('SET_BRIGHTNESS:255\r'.encode())
arduinoSerialData.write('SET_COLOUR:8:0xf00\r'.encode())
