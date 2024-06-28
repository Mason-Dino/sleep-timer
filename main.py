from datetime import *
import customtkinter
import time
import os


root = customtkinter.CTk()
root.title("Timer")
root.geometry("425x210")

root.columnconfigure((0,1,2), weight=1)

timeArea = customtkinter.CTkFrame(root)
timeArea.grid(column=0, row=0, padx=5, pady=5)

workplace = customtkinter.CTkFrame(root)
workplace.grid(column=1, row=0, columnspan=2, padx=5, pady=5)

root.mainloop()