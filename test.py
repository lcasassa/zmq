import serial
ser = serial.Serial('/dev/tty.usbmodem1421', 9600, timeout=0)

while 1:
	x = ser.readline()
	print(x)
