# Turn an Arduino's built-in LED on and off by pushing GUI buttons.
# Works in cooperation with serialbutton.ino on the Arduino side.

# Serial comms library
import serial
# GUI library
import tkinter as tk

# Create a serial object.  Change 'COM7' to match your computer's serial
# port, or use serial.tools.list_ports.comports() to get a list of options.
ser = serial.Serial('COM7',9600,timeout=1)

# Create a window.
window = tk.Tk()
# Create a label, and show it on screen.
label = tk.Label(text='Off!')
label.pack()

# This function is called when the 'On' button is pressed.
def handleon():
	label["text"] = "On!"
	ser.write(b'1')

# This function is called when the 'Off' button is pressed.
def handleoff():
	label["text"] = "Off!"
	ser.write(b'0')

# Create and display the on button
onbutton = tk.Button(text='Turn on',command=handleon)
onbutton.pack()

# Create and display the off button
offbutton = tk.Button(text='Turn off',command=handleoff)
offbutton.pack()

# Start watching the window waiting for button presses.
window.mainloop()