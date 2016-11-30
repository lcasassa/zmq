
import serial

ser = serial.Serial(
        port='/dev/tty.usbmodem1421',\
        baudrate=9600,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=1)

print("connected to: " + ser.portstr)

count = 1
while True:
    x = ser.readline()
    print(str(count) + str(': ') + str(x))
    count = count + 1

ser.close()
