import datetime
import time
import threading  # To run the sound in a separate thread
import winsound 

def convert_to_24_hour_format(time_str):
    return datetime.datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M")

def play_alarm_sound(stop_event):
    while not stop_event.is_set():
        winsound.Beep(frequency=2500, duration=5000)
        time.sleep(1)

def set_alarm(alarm_time_12hr, snooze_minutes=5):
    alarm_time_24hr = convert_to_24_hour_format(alarm_time_12hr)
    print(f"Alarm set for {alarm_time_12hr}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time_24hr:
            print("Time to wake up!")

            # Event to control the alarm sound loop
            stop_event = threading.Event()

            # Start playing the alarm sound in a separate thread
            sound_thread = threading.Thread(target=play_alarm_sound, args=(stop_event,))
            sound_thread.start()

            while True:
                user_input = input("Enter 'snooze' to snooze for 5 minutes or 'stop' to stop the alarm: ").strip().lower()

                if user_input == "snooze":
                    stop_event.set()  # Stop the sound loop
                    sound_thread.join()  # Wait for the sound thread to finish
                    alarm_time_24hr = (datetime.datetime.now() + datetime.timedelta(minutes=snooze_minutes)).strftime("%H:%M")
                    print(f"Snoozed! Next alarm at {alarm_time_24hr}")
                    break  # Exit loop to wait for the next alarm time

                elif user_input == "stop":
                    stop_event.set()  
                    sound_thread.join()  
                    print("Alarm stopped.")
                    return 

                else:
                    print("Invalid input, please enter 'snooze' or 'stop'.")

        time.sleep(1)

alarm_time = input("Enter the time for the alarm (HH:MM AM/PM): ")
set_alarm(alarm_time)
# if __name__ == "__main__":
