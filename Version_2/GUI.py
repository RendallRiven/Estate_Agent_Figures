import tkinter as tk
from tkinter.filedialog import askopenfile
from turtle import pd, right
from PIL import Image, ImageTk
import pandas as pd
from V2_InProgress import *

root=tk.Tk()

canvas = tk.Canvas(root, width=600, height=150)
canvas.grid(columnspan=5)

logo = Image.open('Logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=3, row=0)

User_input = tk.Label(root, text="Enter the first 4 characters of the postcode:", font="Raleway")
User_input.grid(column=0, row=1)

postcode_input = tk.Entry(root)
postcode_input.grid(column=1,row=1)

def open_file():
    browse_text.set('Loading....')
    file = askopenfile(parent=root, mode='rb', title='Choose file', filetype=[('xlsx file', '*.xlsx')])
    if file:
       df =  pd.read_excel(file)

       text_box = tk.Text(root, height=10, width=100, padx=15, pady=15)
       text_box.insert(1.0, df)
       text_box.grid(columnspan=5, row=3)
       browse_text.set('Browse')

browse_text = tk.StringVar()
browse_button = tk.Button(root, textvariable=browse_text, command=lambda:open_file())
browse_text.set("Browse")
browse_button.grid(column=1, row=2)

right_move = tk.Button(root, text='Right_move', command=right_move)
right_move.grid(column=1, row=3)

canvas = tk.Canvas(root, width=600, height=150)
canvas.grid(columnspan=3)

root.mainloop()