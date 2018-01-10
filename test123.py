import serial
import time

arduinoSerialData = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate = 115200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
   )

time.sleep(7)
arduinoSerialData.write('SET_BRIGHTNESS:255\r'.encode())
arduinoSerialData.write('SET_COLOUR:3:0x0f0\r'.encode())
