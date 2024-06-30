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
timeArea.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
timeArea.rowconfigure((0,1,2), weight=1)
timeArea.columnconfigure((0,1,2), weight=1)

timey = 19
timex = 15

h = customtkinter.CTkEntry(timeArea, placeholder_text="Hour")
h.grid(row=0, column=1, pady=timey, padx=timex)

m = customtkinter.CTkEntry(timeArea, placeholder_text="Minute")
m.grid(row=1, column=1, pady=timey, padx=timex)

s = customtkinter.CTkEntry(timeArea, placeholder_text="Second")
s.grid(row=2, column=1, pady=timey, padx=timex)

workplace = customtkinter.CTkFrame(root)
workplace.grid(column=1, row=0, columnspan=2, padx=5, pady=5, sticky="nsew")
workplace.rowconfigure((0,1,2), weight=1)
workplace.columnconfigure((0,1,2), weight=1)

timer = customtkinter.CTkLabel(workplace, text="00:00:00", font=("Arial", 20))
timer.grid(row=0, column=1)

option = customtkinter.CTkFrame(workplace)
option.grid(row=1, column=1, sticky="nsew")
option.rowconfigure((0,1,2), weight=1)

selected_option =  customtkinter.StringVar(value="shut")
optionX = 5
buttonWidth = 15
buttonHeight = 15
buttonChecked = 3

shut = customtkinter.CTkRadioButton(option, text="Shutdown", variable=selected_option, value="shut", font=("Arial", 12), radiobutton_width=buttonWidth, radiobutton_height=buttonHeight, border_width_checked=buttonChecked)
shut.grid(row=0, padx=optionX)

sign = customtkinter.CTkRadioButton(option, text="Sign Out", variable=selected_option, value="sign", font=("Arial", 12), radiobutton_width=buttonWidth, radiobutton_height=buttonHeight, border_width_checked=buttonChecked)
sign.grid(row=1, padx=optionX)

alarm = customtkinter.CTkRadioButton(option, text="Alarm", variable=selected_option, value="alarm", font=("Arial", 12), radiobutton_width=buttonWidth, radiobutton_height=buttonHeight, border_width_checked=buttonChecked)
alarm.grid(row=2, padx=optionX)

start = customtkinter.CTkButton(workplace, text="Start")
start.grid(row=2, column=1)

root.mainloop()