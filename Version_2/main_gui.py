from ctypes.wintypes import SIZE
import tkinter as tk
from tkinter import Button, Frame, Canvas
from tkinter.filedialog import askopenfile
from turtle import bgcolor, pd, right
from PIL import Image, ImageTk
from numpy import pad, size
import pandas as pd
from pyparsing import col
from V2_InProgress import *
import main_gui
print(os.getcwd())
def quit_app():
    root.quit()

def main_gui_run():
    global root
    root=tk.Tk()
    root.title('Data Collection')
    root.iconbitmap(os.getcwd() + "\\Analyte.ico")
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    w = 800 # width for the Tk root
    h = 350 # height for the Tk root
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    canvas = tk.Canvas(root, width=600, height=30)
    canvas.grid(columnspan=3)

    head = Frame(root, width=800, height=215, bg='white')
    head.grid(columnspan=3, rowspan=3, row=0)

    body = Frame(root, width=800, height=199, bg='grey')
    body.grid(columnspan=3, rowspan=4, row=2)

    User_input_url = tk.Label(root,text='URL', font=("shanti", 10), height=1, width=15, bg='white')
    User_input_url.grid(column=1, row =2, pady=10)

    User_input_url = tk.Entry(root, highlightthickness='0.2',width='20')
    User_input_url.configure(highlightbackground='black')
    User_input_url.grid(column=2, row=2)

    postcode = tk.Label(root,text='Postcode', font=("shanti", 10), height=1, width=15, bg='white')
    postcode.grid(column=1, row =3, pady=10)

    postcode_input = tk.Entry(root, highlightthickness='0.2',width='20')
    postcode_input.configure(highlightbackground='black')
    postcode_input.grid(column=2, row = 3)

    right_move_but = Button(root, command=right_move, text="Rightmove", font=("shanti", 10), height=1, width=15, bg='white')
    Disabled = Button(root, text="DISABLED", font=("shanti", 10), height=1, width=15)

    right_move_but.grid(row=4, column=2)
    Disabled.grid(row=4, column=0)

    logo = Image.open('Logo.png')
    logo = logo.resize((150, 150))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(root, image=logo, bg="white")
    logo_label.image = logo
    logo_label.grid(column=0, row=0)

    quit = tk.Button(root, text='Quit', command=quit_app, font=("shanti", 10), height=1, width=10)
    quit.grid(column=1, row=5)


    root.mainloop()

if __name__ == "__main__":
    main_gui_run()
    quit_app()