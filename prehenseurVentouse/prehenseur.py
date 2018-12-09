
import serial


def Aspire():
    ser = serial.Serial('/dev/...', 9600)
    ser.write('1') # python 2, pour python 3 ser.write(b'5')
    ser.close()

def Stop():
    ser = serial.Serial('/dev/...', 9600)
    ser.write('2')  # python 2, pour python 3 ser.write(b'5')
    ser.close()






