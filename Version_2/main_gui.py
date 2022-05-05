from ctypes.wintypes import SIZE
from functools import partial
import tkinter as tk
from tkinter import BOTH, INSERT, Button, Frame, Canvas, Menu, StringVar, Variable
from tkinter import font
from tkinter.filedialog import askopenfile
from turtle import bgcolor, pd, right
from PIL import Image, ImageTk
from numpy import insert, pad, size
import pandas as pd
from pyparsing import col
from V2_InProgress import *
import main_gui
from tkinter import messagebox
import customtkinter
import SQL_query_reporting

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

def quit_app():
    root.destroy()

def main_gui_run():
    global root
    root=customtkinter.CTk()
    root.title('Data Collection')
    root.iconbitmap(os.getcwd() + "\\Analyte.ico")
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    w = 800 # width for the Tk root
    h = 350 # height for the Tk root
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    menubar = Menu(root, background='#ff8000', foreground='black', activebackground='black', activeforeground='black')  
    file = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')  
    file.add_command(label="Exit", command= quit_app)  
    file.add_separator
    menubar.add_cascade(label="File", menu=file)

    settings = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')
    settings.add_command(label="URL settings", command="")
    menubar.add_cascade(label="Settings", menu=settings)

    help = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')
    help.add_command(label="About", command=help_about)
    menubar.add_cascade(label="Help", menu=help)

    canvas = customtkinter.CTkCanvas(root, width=600, height=30)
    canvas.grid(columnspan=3)

    head = customtkinter.CTkFrame(root, width=800, height=220)
    head.grid(columnspan=3, rowspan=4, row=0)

    body = customtkinter.CTkFrame(root, width=800, height=199)
    body.grid(columnspan=3, rowspan=4, row=2)
    
    text_var = tk.StringVar(value="CTkLabel")

    label = tk.Label(root, font=('Arial', 25), text="Housing Analytics tool", bg='#292929', fg='Red')
    label.grid(column=0,columnspan=3, row=1)

    User_input_url = customtkinter.CTkLabel(root,text='URL')
    User_input_url.grid(column=0, row =2, pady=10)

    global url_entry
    url_entry = StringVar()
    User_input_url = customtkinter.CTkEntry(root, textvariable=url_entry)
    User_input_url.grid(column=1, row=2)

    send_url = partial(right_move, url_entry)

    postcode = customtkinter.CTkLabel(root,text='Postcode')
    postcode.grid(column=0, row =3, pady=10)

    global postcode_entry
    postcode_entry = StringVar()
    postcode_input = customtkinter.CTkEntry(root, textvariable = postcode_entry)
    postcode_input.grid(column=1, row = 3)

    send_postcode = partial(right_move_postcode, postcode_entry)

    right_move_but = customtkinter.CTkButton(root, command=send_url, text="Rightmove")
    right_move_but.grid(row=2, column=2)
    Disabled = customtkinter.CTkButton(root, text="DISABLED") 
    Disabled.grid(row=3, column=2)

    Download_all = customtkinter.CTkButton(root, text='Download all time data', command=SQL_query_reporting.DB_download)
    Download_all.grid(column=1, row= 4)

    root.config(menu=menubar)
    root.mainloop()

def help_about(): 
    global rooty    
    rooty=customtkinter.CTk()
    rooty.title('About')
    rooty.iconbitmap(os.getcwd() + "\\Analyte.ico")
    ws = rooty.winfo_screenwidth() # width of the screen
    hs = rooty.winfo_screenheight() # height of the screen
    w = 215 # width for the Tk root
    h = 80 # height for the Tk root
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    rooty.geometry('%dx%d+%d+%d' % (w, h, x, y)) #Geometer is used to set where the application will open on the screen


    text = customtkinter.CTkLabel(rooty, text="Analyte.uk \n Estate agents data analytics tool. \n Version 1.01 \n All rights reserved")  
    text.grid(column=1, row=1)

    rooty.wm_protocol("WM_DELETE_WINDOW", destory_window)
    rooty.mainloop()
    
def destory_window():
    rooty.destroy()

if __name__ == "__main__":
    main_gui_run()
