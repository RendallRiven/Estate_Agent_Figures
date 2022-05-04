
from tkinter import *
from ctypes.wintypes import SIZE
import tkinter as tk
from tkinter import Frame, Canvas
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from turtle import bgcolor, pd, right, width
from PIL import Image, ImageTk
from numpy import pad, size
import pandas as pd
from V2_InProgress import *
from functools import partial
import sqlite3
import customtkinter
from main_gui import main_gui_run
from winreg import *


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


def validateLogin(username, password):
    user = username.get()
    pword = password.get()
    
    con = sqlite3.connect("C:\SQLite\EST_database.db")
    cur = con.cursor()
    statement = f"Select username from users where username='{user}' and password= '{pword}'"
    cur.execute(statement)
    if not cur.fetchone():
        messagebox.showerror("Login Failed", message="Incorrect username/password combination, try again.")
    else:
        next_gui(rooty)

def login():
    global rooty
    rooty=customtkinter.CTk()
    rooty.title('Login')
    rooty.iconbitmap(os.getcwd() + "\\Analyte.ico")
    global label
    label = tk.Label(rooty, text="Light Mode on")
    ws = rooty.winfo_screenwidth() # width of the screen
    hs = rooty.winfo_screenheight() # height of the screen
    w = 350 # width for the Tk root
    h = 150 # height for the Tk root
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    rooty.geometry('%dx%d+%d+%d' % (w, h, x, y)) #Geometer is used to set where the application will open on the screen
    rooty.columnconfigure(0, weight=1)   # Set weight to row and 
    rooty.rowconfigure(0, weight=1)  

    usernamelabel = customtkinter.CTkLabel(text="Username").grid(column=0, row=2)
    username = StringVar()
    usernameentry = customtkinter.CTkEntry(rooty, textvariable=username).grid(column=1, row=2, padx=5,pady=5,ipadx=5)
    
    passwordlabel = customtkinter.CTkLabel(text='Password').grid(column=0, row=5)
    password = StringVar()
    passwordentry = customtkinter.CTkEntry(rooty, show='#', textvariable=password).grid(column=1, row=5,padx=5,pady=5,ipadx=5)

    validate = partial(validateLogin, username, password)

    Login = customtkinter.CTkButton(rooty, text ="Login", command = validate) 
    Login.grid(column=0, row=8,pady = 10,)
    
    exit_button = customtkinter.CTkButton(rooty, text="Quit", command = rooty.quit)
    exit_button.grid(column=1,row=8,pady=10, padx=50)

    rooty.mainloop()

def next_gui(rooty):
    rooty.destroy()
    main_gui_run()

login()

