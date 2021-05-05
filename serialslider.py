# Blink an Arduino's built-in LED for an amount of time determined by a GUI
# slider.
# Works in cooperation with serialslider.ino on the Arduino side.

# Serial comms library
import serial
# GUI library
import tkinter as tk

# Create a serial object.  Change 'COM7' to match your computer's serial
# port, or use serial.tools.list_ports.comports() to get a list of options.
ser = serial.Serial('COM7',9600,timeout=1)
# Create a window and a slider ('scale'), and show it on screen.
window = tk.Tk()
scale = tk.Scale(orient='horizontal')
scale.pack()

# This function is called when the 'Blink' button is pressed.
def handleblink():
	ser.write(bytes([scale.get()]))

# Create and display the Blink button
blinkbutton = tk.Button(text='Blink',command=handleblink)
blinkbutton.pack()

# Start watching the window waiting for button presses.
window.mainloop()