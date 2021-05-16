from tkinter import *
from functools import partial
from tkinter import ttk
import platform
import serial


def connectByUART() -> None:
    global ser
    global baudrate
    if (platform.system().startswith("Win")):
        port = portCmbox.get()
    else:
        port = "dev/ttypUSB0"
    if not ser.is_open:
        try:
            baudrate = baudrateCmbox.get()
            ser = serial.Serial(port,baudrate)
            statusLabel['text'] = "Connection established!"
        except:
            statusLabel['text'] = "Connection could not be established."
    else:
        if baudrate != baudrateCmbox.get():
            ser.close()
            connectByUART()
        else:
            statusLabel['text'] = "Connection already opened!"

def sendCommand(command):
    try:
        ser.write(command)
        statusLabel["text"] = "Command sent."
    except:
        statusLabel["text"] = "Error sending command!"

#Global variables
ser = serial.Serial()
baudrate = 0

root = Tk()
root.title("Robotic Arm Controller")


controlFrame = LabelFrame(text="Control")
connectionFrame = LabelFrame(text="Communication")
statusLabel = Label(root,text="",relief=SUNKEN,anchor=W)


baudrateCmbox = ttk.Combobox(connectionFrame,values=[9600,19200,38400,57600,115200],state="readonly")
baudrateCmbox.current(0)
portCmbox = ttk.Combobox(connectionFrame,values=["COM3","COM4","COM5","COM6","COM7"],state="readonly")
portCmbox.current(1)

connectBtn = Button(connectionFrame,text="Connect",command=connectByUART)


#Control widgets
aButton = Button(controlFrame,text="A toggle",command=partial(sendCommand,b'a'))
bButton = Button(controlFrame,text="B toggle",command=partial(sendCommand,b'b'))
cButton = Button(controlFrame,text="C toggle",command=partial(sendCommand,b'c'))


#Positioning widgets
controlFrame.grid(row=0,column=0,padx=5,pady=5)
connectionFrame.grid(row=0,column=1,padx=5,pady=5)
statusLabel.grid(row=2,column=0,sticky=W+E,columnspan=3,padx=5)
aButton.grid(row=0,column=0,padx=5,pady=5,sticky=W+E+N+S)
bButton.grid(row=0,column=1,padx=5,pady=5,sticky=E+W+N+S)
cButton.grid(row=0,column=2,padx=5,pady=5,sticky=E+W+N+S)

connectBtn.grid(row=2,column=0,sticky=W+E,padx=5,pady=5)
baudrateCmbox.grid(row=1,column=0,sticky=W+E,padx=5,pady=5)
portCmbox.grid(row=0,column=0,sticky=W+E,padx=5,pady=5)

root.mainloop()
