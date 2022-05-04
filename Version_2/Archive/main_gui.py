from ctypes.wintypes import SIZE
import tkinter as tk
from tkinter import BOTH, INSERT, Button, Frame, Canvas, Menu
from tkinter.filedialog import askopenfile
from turtle import bgcolor, pd, right
from PIL import Image, ImageTk
from numpy import insert, pad, size
import pandas as pd
from pyparsing import col

import main_gui
from tkinter import messagebox
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
root_tk = customtkinter.CTk()
root_tk.geometry(f"{600}x{500}")
root_tk.title("CTk example")



root_tk.mainloop()
