import serial
import tkinter as tk

ser = serial.Serial('COM7',9600,timeout=1)
window = tk.Tk()
scale = tk.Scale(orient='horizontal')
scale.pack()

def handleblink():
	ser.write(bytes([scale.get()]))

blinkbutton = tk.Button(text='Blink',command=handleblink)
blinkbutton.pack()

window.mainloop()