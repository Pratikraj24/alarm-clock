import tkinter as tk
from tkinter import ttk
import time
import winsound
import threading

# Function to set the alarm
def set_alarm():
    alarm_time = entry.get()
    selected_tone = tone_var.get()
    alarm_label.config(text="Alarm set for " + alarm_time)
    
    def alarm_check():
        while True:
            current_time = time.strftime("%H:%M")
            if current_time == alarm_time:
                for i in range(5):  # Sound alert 5 times
                    if selected_tone == "Beep":
                        winsound.Beep(1000, 1000)  # Beep sound
                    elif selected_tone == "System Exclamation":
                        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                    elif selected_tone == "System Hand":
                        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
                    elif selected_tone == "System Question":
                        winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                    elif selected_tone == "System Asterisk":
                        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
                    elif selected_tone == "System Exit":
                        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                    elif selected_tone == "Custom Tone 1":
                        winsound.PlaySound("custom_tone_1.wav", winsound.SND_FILENAME)
                    elif selected_tone == "Custom Tone 2":
                        winsound.PlaySound("custom_tone_2.wav", winsound.SND_FILENAME)
                    time.sleep(1)  # Wait a second between sounds
                alarm_label.config(text="Alarm Ringing!")
                break
            time.sleep(1)  # Check every second
    
    # Run the alarm_check function in a separate thread to avoid blocking the GUI
    threading.Thread(target=alarm_check).start()

# Function to stop the alarm
def stop_alarm():
    alarm_label.config(text="Alarm Stopped")

# Creating the main window with a medium size
root = tk.Tk()
root.title("Python Alarm Clock")
root.geometry("300x250")  # Width x Height

# Creating the labels and entry for alarm time
label = tk.Label(root, text="Enter alarm time (HH:MM):")
label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

# Dropdown menu for selecting alarm tone
tone_label = tk.Label(root, text="Select alarm tone:")
tone_label.pack(pady=5)
tone_var = tk.StringVar()
tone_var.set("Beep")  # Default value
tone_options = ["Beep", "System Exclamation", "System Hand", "System Question", "System Asterisk", "System Exit", "Custom Tone 1", "Custom Tone 2"]
tone_menu = ttk.Combobox(root, textvariable=tone_var, values=tone_options, state="readonly")
tone_menu.pack(pady=5)

# Label to show alarm status
alarm_label = tk.Label(root, text="")
alarm_label.pack(pady=10)

# Buttons to set and stop the alarm
set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=5)
stop_button = tk.Button(root, text="Stop Alarm", command=stop_alarm)
stop_button.pack(pady=5)

# Run the application
root.mainloop()
