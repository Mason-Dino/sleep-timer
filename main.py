from datetime import *
import customtkinter
import winsound
import pygame
import time
import os

# Set up the GUI
root = customtkinter.CTk()
root.title("Timer")
root.geometry("425x210")
customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")
root.after(201, lambda :root.iconbitmap('C:/Users/norbe/OneDrive/Desktop/sleep-timer/logo_new.ico'))
root.columnconfigure((0,1,2), weight=1)

# Set up the time space in gui area
timeArea = customtkinter.CTkFrame(root)
timeArea.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
timeArea.rowconfigure((0,1,2), weight=1)
timeArea.columnconfigure((0,1,2), weight=1)

timey = 19
timex = 15

# Set up the time fields
h = customtkinter.CTkEntry(timeArea, placeholder_text="Hour")
h.grid(row=0, column=1, pady=timey, padx=timex)

m = customtkinter.CTkEntry(timeArea, placeholder_text="Minute")
m.grid(row=1, column=1, pady=timey, padx=timex)

s = customtkinter.CTkEntry(timeArea, placeholder_text="Second")
s.grid(row=2, column=1, pady=timey, padx=timex)

# Set up the options, timer label, and main button
workplace = customtkinter.CTkFrame(root)
workplace.grid(column=1, row=0, columnspan=2, padx=5, pady=5, sticky="nsew")
workplace.rowconfigure((0,1,2), weight=1)
workplace.columnconfigure((0,1,2), weight=1)

timer = customtkinter.CTkLabel(workplace, text="00:00:00", font=("Arial", 20))
timer.grid(row=0, column=1)

option = customtkinter.CTkFrame(workplace)
option.grid(row=1, column=1, sticky="nsew")
option.rowconfigure((0,1,2), weight=1)

# Set up the radio buttons
selected_option =  customtkinter.StringVar(value="shut")
optionX = 5
buttonWidth = 15
buttonHeight = 15
buttonChecked = 3

shut = customtkinter.CTkRadioButton(option, text="Shutdown", variable=selected_option, value="shut", font=("Arial", 12), radiobutton_width=buttonWidth, radiobutton_height=buttonHeight, border_width_checked=buttonChecked, border_width_unchecked=3, 
                                    fg_color=["#3B8ED0", "#1F6AA5"], hover_color=["#36719F", "#144870"], text_color=["gray10", "#DCE4EE"], border_color=["#3E454A", "#949A9F"], text_color_disabled=["gray60", "gray45"], corner_radius=1000)
shut.grid(row=0, padx=optionX)

sign = customtkinter.CTkRadioButton(option, text="Sign Out", variable=selected_option, value="sign", font=("Arial", 12), radiobutton_width=buttonWidth, radiobutton_height=buttonHeight, border_width_checked=buttonChecked, border_width_unchecked=3,
                                    fg_color=["#3B8ED0", "#1F6AA5"], hover_color=["#36719F", "#144870"], text_color=["gray10", "#DCE4EE"], border_color=["#3E454A", "#949A9F"], text_color_disabled=["gray60", "gray45"], corner_radius=1000)
sign.grid(row=1, padx=optionX)

alarm = customtkinter.CTkRadioButton(option, text="Alarm", variable=selected_option, value="alarm", font=("Arial", 12), radiobutton_width=buttonWidth, radiobutton_height=buttonHeight, border_width_checked=buttonChecked, border_width_unchecked=3,
                                    fg_color=["#3B8ED0", "#1F6AA5"], hover_color=["#36719F", "#144870"], text_color=["gray10", "#DCE4EE"], border_color=["#3E454A", "#949A9F"], text_color_disabled=["gray60", "gray45"], corner_radius=1000)
alarm.grid(row=2, padx=optionX)

totalSec = 0
stopTime = True
mainButton = None

def startTime():
    """
    This function is called when the user clicks the "Start" button.
    It retrieves the values entered in the hour, minute, and second fields.
    It calculates the total seconds based on the entered values.
    It sets the timer label to display the entered values.
    It sets the stopTime flag to False.
    If the entered values are all zero, it does nothing.
    Otherwise, it changes the text of the main button to "Stop" and calls the updateTimer function.
    """
    global totalSec
    global TimeStamp
    global stopTime

    # Get the hour value from the hour field
    if h.get() == "":
        hourTime = 0
    else:
        hourTime = int(h.get())

    # Get the minute value from the minute field
    if m.get() == "":
        minTime = 0
    else:
        minTime = int(m.get())

    # Get the second value from the second field
    if s.get() == "":
        secTime = 0
    else:
        secTime = int(s.get())

    # Set the text of the timer label to display the entered values
    timer.configure(text=f"{hourTime:02}:{minTime:02}:{secTime:02}")

    # Calculate the total seconds based on the entered values
    totalSec = (hourTime * 60 * 60) + (minTime * 60) + secTime

    # Get the current date and time
    timeNow = datetime.now()

    # Construct a string representing the current date and time, with the entered values appended
    TimeStamp = datetime.strptime(
        f"""{timeNow.strftime("%m")}/{timeNow.strftime("%d")}/{timeNow.strftime("%Y")} {hourTime}:{minTime}:{secTime}""",
        "%m/%d/%Y %H:%M:%S"
    )

    # Set the stopTime flag to False
    stopTime = False

    # If all entered values are zero, do nothing
    if hourTime == 0 and minTime == 0 and secTime == 0:
        pass
    else:
        # Change the text of the main button to "Stop" and configure its command to call the stopTimer function
        mainButton.configure(text="Stop", command=stopTimer)

        # Call the updateTimer function to start the timer
        updateTimer()

def updateTimer():
    """
    This function updates the timer by decreasing the total seconds by 1 every second.
    It also updates the timer label with the current time remaining.
    If the total seconds reaches 0, it stops the timer and performs the selected action.
    """
    global totalSec  # Declare the variables as global so they can be modified in this function
    global TimeStamp
    global stopTime

    if stopTime == False:  # Check if the timer is not stopped
        totalSec -= 1  # Decrease the total seconds by 1

        TimeStamp = TimeStamp - timedelta(seconds=1)  # Decrease the TimeStamp by 1 second

        timer.configure(text=TimeStamp.strftime("%H:%M:%S"))  # Update the timer label with the current time remaining

        repeat = root.after(1000, updateTimer)  # Schedule the next update after 1 second

        if totalSec <= 0:  # Check if the total seconds have reached 0
            root.after_cancel(repeat)  # Cancel the scheduled update
            timer.configure(text="00:00:00")  # Reset the timer label

            if selected_option.get() == "shut":  # Check if the selected action is to shutdown
                os.system("shutdown /s /t 1")  # Shutdown the computer

            if selected_option.get() == "sign":  # Check if the selected action is to sign out
                os.system("shutdown -l")  # Sign out of the computer

            if selected_option.get() == "alarm":  # Check if the selected action is to play an alarm
                # Two options for how to play the audio:

                # winsound.PlaySound(r'alarm.wav', winsound.SND_ASYNC)  # Play the alarm using the winsound library

                pygame.mixer.init()  # Initialize the pygame mixer
                sounda= pygame.mixer.Sound("alarm.mp3")  # Load the alarm sound file
                sounda.play()  # Play the alarm sound

def stopTimer():
    """
    This function stops the timer by setting the stopTime flag to True,
    resetting the timer label to "00:00:00", and resetting the total seconds
    to 5. It also changes the text of the main button to "Start" and sets
    its command to the startTime function.
    """
    # Set the stopTime flag to True to stop the timer
    global stopTime
    stopTime = True

    # Reset the timer label to "00:00:00"
    timer.configure(text="00:00:00")

    # Reset the total seconds to 5
    global totalSec
    totalSec = 5

    # Change the text of the main button to "Start"
    mainButton.configure(text="Start")

    # Set the command of the main button to the startTime function
    mainButton.configure(command=startTime)


mainButton = customtkinter.CTkButton(workplace, text="Start", command=startTime)
mainButton.grid(row=2, column=1)

root.mainloop()