# importing only those functions
# which are needed
from tkinter import Tk as tk
from tkinter.ttk import *  
from ctypes.wintypes import SIZE
import tkinter as tk
from tkinter import Frame, Canvas
from tkinter.filedialog import askopenfile
from turtle import bgcolor, pd, right
from login_tkinter_gui import *
# creating tkinter window

rooty=tk.Tk()
rooty.title('Data Collection')

frame = Frame(rooty)
frame.pack()

def next_gui():
    rooty.destroy()
    from login_tkinter_gui import main_screen
    

canvas = Canvas(rooty, bg='yellow', width=300, height=300)
  
# Creating button. In this destroy method is passed
# as command, so as soon as button 1 is pressed root
# window will be destroyed
btn1 = Button(rooty, text ="Button 1", command = next_gui())
btn1.pack(pady = 10)
  
# Creating button. In this destroy method is passed
# as command, so as soon as button 2 is pressed
# button 1 will be destroyed
btn2 = Button(canvas, text ="Button 2", command = canvas.destroy)
btn2.pack(pady = 10)
  
# infinite loop
rooty.mainloop()

if __name__ == '__main__':
    next_gui()