import time
import serial
import Tkinter

ser = serial.Serial('/dev/ttyACM1', 115200) #  tools = port "COM4?"

def Aspire():

    time.sleep(0)
    ser.write('1') # python 2, pour python 3 ser.write(b'5')

def Stop():
    time.sleep(0)
    ser.write('2')  # python 2, pour python 3 ser.write(b'5')


#input("entrer pour quitter")

