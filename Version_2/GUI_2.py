from ctypes.wintypes import SIZE
import tkinter as tk
from tkinter import Frame, Canvas
from tkinter.filedialog import askopenfile
from turtle import bgcolor, pd, right
from PIL import Image, ImageTk
from numpy import pad, size
import pandas as pd
from V2_InProgress import *

def quit_app():
    root.quit()

root=tk.Tk()
root.title('Data Collection')

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg='yellow', width=300, height=300)
canvas.pack()

logo = Image.open('Logo.png')
logo = logo.resize((150, 150))
logo = ImageTk.PhotoImage(logo)
canvas.create_image(15, 150, image=logo)

User_input = tk.Label(canvas, text="Postcode:", font=("Raleway","8"))
User_input.pack(padx=20, pady=150)

postcode_input = tk.Entry(canvas, highlightthickness='0.5',width='10')
postcode_input.configure(highlightbackground='red')
postcode_input.pack(padx=20,pady=(90)

User_input_url = tk.Label(canvas,text='URL', font=('raleway', '8'))
User_input_url.pack(padx=100,pady=90)

right_move = tk.Button(canvas, text='Right_move', command=right_move)
right_move.pack(padx=20,pady=80)

quit = tk.Button(canvas, text='Quit', command=quit_app)
quit.pack(padx=100,pady=100)

root.mainloop()
