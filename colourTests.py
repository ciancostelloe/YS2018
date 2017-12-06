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

arduinoSerialData.write('SET_BRIGHTNESS:255\r'.encode())
time.sleep(0.2)
arduinoSerialData.write('SET_COLOUR:9:0xf00\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0xe00\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0xd00\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0xc00\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0xb00\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0xa00\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x900\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x800\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x700\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x600\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x500\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x400\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x300\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x200\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x100\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x000\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x010\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x020\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x030\r'.encode())
time.sleep(0.2)

arduinoSerialData.write('SET_COLOUR:9:0x040\r'.encode())
time.sleep(0.2)
