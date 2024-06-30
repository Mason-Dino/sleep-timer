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

totalSec = 0
stopTime = True
mainButton = None

def startTime():
    global totalSec
    global TimeStamp
    global stopTime

    if h.get() == "":
        hourTime = 0

    else:
        hourTime = int(h.get())

    if m.get() == "":
        minTime = 0

    else:
        minTime = int(m.get())

    if s.get() == "":
        secTime = 0

    else:
        secTime = int(s.get())

    timer.configure(text=f"{hourTime:02}:{minTime:02}:{secTime:02}")

    totalSec = (hourTime * 60 * 60) + (minTime * 60) + secTime
    timeNow = datetime.now()
    TimeStamp = datetime.strptime(f"""{timeNow.strftime("%m")}/{timeNow.strftime("%d")}/{timeNow.strftime("%Y")} {hourTime}:{minTime}:{secTime}""", "%m/%d/%Y %H:%M:%S")
    stopTime = False

    mainButton.configure(text="Stop", command=stopTimer)
    
    updateTimer()

def updateTimer():
    global totalSec
    global TimeStamp
    global stopTime

    if stopTime == False:
        totalSec -= 1

        TimeStamp = TimeStamp - timedelta(seconds=1)

        timer.configure(text=TimeStamp.strftime("%H:%M:%S"))

        repeat = root.after(100, updateTimer)

        if totalSec <= 0:
            root.after_cancel(repeat)
            timer.configure(text="00:00:00")

            if selected_option.get() == "shut":
                os.system("shutdown /s /t 1")

            if selected_option.get() == "sign":
                os.system("shutdown -l")

            if selected_option.get() == "alarm":
                print("coming soon")

def stopTimer():
    global stopTime
    global totalSec

    stopTime = True

    timer.configure(text="00:00:00")
    totalSec = 5

    mainButton.configure(text="Start", command=startTime)


mainButton = customtkinter.CTkButton(workplace, text="Start", command=startTime)
mainButton.grid(row=2, column=1)

root.mainloop()