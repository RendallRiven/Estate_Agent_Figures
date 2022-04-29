from tkinter import *
from ctypes.wintypes import SIZE
import tkinter as tk
from tkinter import Frame, Canvas
from tkinter.filedialog import askopenfile
from turtle import bgcolor, pd, right, width
from PIL import Image, ImageTk
from numpy import pad, size
import pandas as pd
from V2_InProgress import *

def login():
    rooty=tk.Tk()
    rooty.title('Data Collection')
    rooty.geometry('200x100')
    rooty.columnconfigure(0, weight=1)   # Set weight to row and 
    rooty.rowconfigure(0, weight=1)  

    Label(text="Username").grid(column=0, row=2)
    tk.Entry(rooty).grid(column=1, row=2, padx=5,pady=5,ipadx=5)
    
    Label(text='Password').grid(column=0, row=5)
    tk.Entry(rooty).grid(column=1, row=5,padx=5,pady=5,ipadx=5)
    # Creating button. In this destroy method is passed
    # as command, so as soon as button 1 is pressed root
    # window will be destroyed
    Login = Button(rooty, text ="Login", command = lambda : next_gui(rooty))
    Login.grid(column=0, row=8,pady = 10,)
    
    exit_button = Button(rooty, text="Quit", command = rooty.quit())
    exit_button.grid(column=1,row=8,pady=10, padx=50)

    # infinite loop
    rooty.mainloop()
'''def second_screen():
    root=tk.Tk()
    root.title('Data Collection')

    frame = Frame(root)
    frame.pack()

    canvas = Canvas(frame, bg='yellow', width=300, height=300)

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
'''


def next_gui(rooty):
    rooty.destroy()
    main_screen()

login()