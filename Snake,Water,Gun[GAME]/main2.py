import datetime
import time
import threading
import winsound
import tkinter as tk
from tkinter import messagebox

def convert_to_24_hour_format(time_str):
    return datetime.datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M")

def play_alarm_sound(stop_event):
    while not stop_event.is_set():
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        time.sleep(1)

def set_alarm():
    alarm_time_12hr = alarm_entry.get()
    snooze_minutes = 5  # Default snooze time
    alarm_time_24hr = convert_to_24_hour_format(alarm_time_12hr)
    print(f"Alarm set for {alarm_time_12hr}")
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time_24hr:
            print("Time to wake up!")
            stop_event = threading.Event()
            sound_thread = threading.Thread(target=play_alarm_sound, args=(stop_event,))
            sound_thread.start()

            # Disable set button during alarm
            set_button.config(state=tk.DISABLED)
            
            while True:
                user_response = messagebox.askquestion("Alarm", "Time to wake up! Snooze for 5 minutes?")
                if user_response == 'yes':
                    stop_event.set()
                    sound_thread.join()
                    alarm_time_24hr = (datetime.datetime.now() + datetime.timedelta(minutes=snooze_minutes)).strftime("%H:%M")
                    print(f"Snoozed! Next alarm at {alarm_time_24hr}")
                    break  # Exit inner loop to wait for the new alarm time
                else:
                    stop_event.set()
                    sound_thread.join()
                    print("Alarm stopped.")
                    set_button.config(state=tk.NORMAL)  # Re-enable set button
                    return  # Exit the program

        time.sleep(1)

def start_alarm():
    alarm_thread = threading.Thread(target=set_alarm)
    alarm_thread.start()

# GUI Setup
root = tk.Tk()
root.title("Alarm Clock")

frame = tk.Frame(root)
frame.pack(pady=20)

alarm_label = tk.Label(frame, text="Enter Alarm Time (HH:MM AM/PM):")
alarm_label.pack(side=tk.LEFT)

alarm_entry = tk.Entry(frame)
alarm_entry.pack(side=tk.LEFT)

set_button = tk.Button(frame, text="Set Alarm", command=start_alarm)
set_button.pack(side=tk.LEFT)

root.mainloop()
