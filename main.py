from datetime import *
import customtkinter
import time
import os


root = customtkinter.CTk()
root.title("Timer")
root.geometry("425x210")
root

root.columnconfigure((0,1,2), weight=1)

timeArea = customtkinter.CTkFrame(root)
timeArea.grid(column=0, row=0, padx=5, pady=5)
timeArea.rowconfigure((0,1,2), weight=1)

timey = 19
timex = 15

h = customtkinter.CTkEntry(timeArea, placeholder_text="Hour")
h.grid(row=0, column=0, pady=timey, padx=timex)

m = customtkinter.CTkEntry(timeArea, placeholder_text="Minute")
m.grid(row=1, column=0, pady=timey, padx=timex)

s = customtkinter.CTkEntry(timeArea, placeholder_text="Second")
s.grid(row=2, column=0, pady=timey, padx=timex)

workplace = customtkinter.CTkFrame(root)
workplace.grid(column=1, row=0, columnspan=2, padx=5, pady=5)
workplace.columnconfigure((0,1,2), weight=1)
workplace.rowconfigure((0,1), weight=1)

start = customtkinter.CTkButton(workplace, text="Start")
start.grid(row=1, column=0, columnspan=2)

root.mainloop()