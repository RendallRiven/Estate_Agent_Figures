from ctypes.wintypes import SIZE
import tkinter as tk
from tkinter.filedialog import askopenfile
from turtle import bgcolor, pd, right
from PIL import Image, ImageTk
from numpy import pad, size
import pandas as pd
from V2_InProgress import *

root=tk.Tk()
root.title('Data Collection')

logo = Image.open('Logo.png')
logo = logo.resize((150, 150))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0, rowspan=3)

User_input = tk.Label(root, text="Postcode:", font=("Raleway","8"))
User_input.grid(column=1, row=1)

postcode_input = tk.Entry(root, highlightthickness='0.5',width='10')
postcode_input.configure(highlightbackground='red')
postcode_input.grid(column=2,row=1, pady=(20,20))

User_input_url = tk.Label(root,text='URL', font=('raleway', '8'))
User_input_url.grid(column=1, row=2)

def quit_app():
    root.quit()

right_move = tk.Button(root, text='Right_move', command=right_move)
right_move.grid(column=2, row=2)

quit = tk.Button(root, text='Quit', command=quit_app)
quit.grid(column=2, row=3)

root.mainloop()
