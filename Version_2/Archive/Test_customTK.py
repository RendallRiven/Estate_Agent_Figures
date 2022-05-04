import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
root_tk.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

text_var = tkinter.StringVar(value="CTkLabel")

label = customtkinter.CTkLabel(master=root_tk,
                               variable=text_var,
                               width=120,
                               height=25,
                               fg_color=("white", "gray75"),
                               corner_radius=8)
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()