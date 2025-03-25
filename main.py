import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import winsound  # For sound alarms on Windows
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar

# not alarming in the time that it was set
# fix the text
# Check timers periodically
def check_timers():
    now = datetime.now()
    for task, alarm_time in list(alarms.items()):
        # If the alarm time is in the past, set it for the next day
        if alarm_time < now:
            alarm_time += timedelta(days=1)

        # Calculate the time difference
        time_difference = (alarm_time - now).total_seconds()
        
        if time_difference > 0:  # If the time is in the future
            hours, remainder = divmod(int(time_difference), 3600)
            minutes, seconds = divmod(remainder, 60)
            timer_label.config(text=f"Timer for '{task}': {hours:02}:{minutes:02}:{seconds:02}")
        else:
            trigger_timer(task)
            del alarms[task]  # Remove the timer after triggering
    root.after(1000, check_timers)  # Check every second

# Update the current time display
def update_current_time():
    now = datetime.now()
    current_time_label.config(text=f"Current Time: {now.strftime('%H:%M:%S')}")
    root.after(1000, update_current_time)  # Update every second

# Trigger timer for the given task
def trigger_timer(task):
    # Show a reminder popup
    messagebox.showinfo("Timer", f"Time's up for: {task}!")
    # Play a beep sound
    for _ in range(3):  # Beep 3 times
        winsound.Beep(1000, 500)

# Add task to the list
def add_task():
    task = task_entry.get()
    selected_date = date_entry.get_date()  # Get the selected date
    alarm_hour = hour_spinbox.get()
    alarm_minute = minute_spinbox.get()
    
    if not task:
        messagebox.showwarning("Input Error", "Task cannot be empty!")
        return
    
    try:
        # Create a datetime object for the alarm
        alarm_datetime = datetime(selected_date.year, selected_date.month, selected_date.day, int(alarm_hour), int(alarm_minute))
        alarms[task] = alarm_datetime
        task_listbox.insert(tk.END, f"{task} - {alarm_hour}:{alarm_minute} on {selected_date}")  # Show task with alarm time
        task_entry.delete(0, tk.END)
        
        # Reset hour and minute Spinboxes
        hour_spinbox.delete(0, tk.END)
        hour_spinbox.insert(0, "00")  # Reset hour to "00"
        minute_spinbox.delete(0, tk.END)
        minute_spinbox.insert(0, "00")  # Reset minute to "00"
        
    except ValueError:
        messagebox.showerror("Input Error", "Invalid time selected!")
        return

# Delete selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showwarning("Selection Error", "No task selected!")
        return
    task_with_time = task_listbox.get(selected_task_index)
    task = task_with_time.split(" - ")[0]  # Extract task name
    task_listbox.delete(selected_task_index)
    if task in alarms:
        del alarms[task]

# Center the window on the screen
def center_window(width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

# Initialize main tkinter window
root = tk.Tk()
root.title("To-Do List Manager with Timers")

# Center the window
center_window(400, 400)

# Task list and timers storage
alarms = {}

# Task input
task_label = tk.Label(root, text="Task:")
task_label.grid(row=0, column=0, padx=5, pady=5)
task_entry = tk.Entry(root, width=30)
task_entry.grid(row=0, column=1, padx=5, pady=5)

# Date input
date_label = tk.Label(root, text="Select Date:")
date_label.grid(row=2, column=0, padx=5, pady=5)
date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=2, column=1, padx=5, pady=5)

# Time input
time_label = tk.Label(root, text="Select Time:")
time_label.grid(row=3, column=0, padx=5, pady=5)

# Hour Spinbox
hour_spinbox = tk.Spinbox(root, from_=0, to=23, width=5, format='%02.0f')
hour_spinbox.grid(row=3, column=1, padx=5, pady=5)

# Minute Spinbox
minute_spinbox = tk.Spinbox(root, from_=0, to=59, width=5, format='%02.0f')
minute_spinbox.grid(row=3, column=2, padx=5, pady=5)

# Timer display label
timer_label = tk.Label(root, text="", font=("Helvetica", 12))
timer_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Current time display label
current_time_label = tk.Label(root, text="", font=("Helvetica", 12))
current_time_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

# Task listbox
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=7, column=0, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=7, column=1, padx=5, pady=5)

# Start timer checking loop
root.after(1000, check_timers)

# Start updating current time
update_current_time()

# Run the application
root.mainloop()
