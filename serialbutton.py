import serial
import tkinter as tk

ser = serial.Serial('COM7',9600,timeout=1)
window = tk.Tk()
label = tk.Label(text='Off!')
label.pack()

def handleon():
	label["text"] = "On!"
	ser.write(b'1')

def handleoff():
	label["text"] = "Off!"
	ser.write(b'0')

onbutton = tk.Button(text='Turn on',command=handleon)
onbutton.pack()

offbutton = tk.Button(text='Turn off',command=handleoff)
offbutton.pack()

window.mainloop()