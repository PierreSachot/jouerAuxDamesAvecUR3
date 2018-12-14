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


control_window=Tkinter.Tk()
Button = Tkinter.Button

btn1=Button(control_window,text="Aspire",command=Aspire)
btn2=Button(control_window,text="Stop",command=Stop)

btn1.grid(row=0,column=1)
btn2.grid(row=0,column=2)

control_window.mainloop()


#input("entrer pour quitter")

