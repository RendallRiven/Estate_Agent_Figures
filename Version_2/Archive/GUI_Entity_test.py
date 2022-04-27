from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter.filedialog import askopenfile
from turtle import pd, right
from PIL import Image, ImageTk
import pandas as pd


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

v = tk.StringVar()
postcode_input = tk.Entry(root, textvariable=v)
postcode_input.grid(column=1,row=1)

value = v.get()

print(value)

text_box = tk.Text(root, height=10, width=100, padx=15, pady=15)
text_box.insert(1.0, value)
text_box.grid(columnspan=5, row=3)


canvas = tk.Canvas(root, width=600, height=150)
canvas.grid(columnspan=3)

root.mainloop()