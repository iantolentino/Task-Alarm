
# To-Do List Manager with Timers

A simple and intuitive To-Do List Manager with built-in timers, designed to help you stay organized and on schedule. This application allows you to add tasks, set specific dates and times for reminders, and receive alerts when the timer expires. Perfect for managing daily tasks, deadlines, or personal reminders.

---

## Features

- **Task Management**: Add and delete tasks with ease.
- **Date and Time Selection**: Set specific dates and times for task reminders using a calendar and spinboxes.
- **Timer Alerts**: Receive pop-up notifications and sound alerts when the timer expires.
- **Real-Time Updates**: Displays the current time and countdown for active timers.
- **User-Friendly Interface**: Clean and intuitive design for seamless task management.

---

## Requirements

- Python 3.x
- `tkinter` (included with Python)
- `tkcalendar` (install via `pip install tkcalendar`)
- `winsound` (for Windows sound alerts; included with Python on Windows)

---

## Installation

1. **Clone the repository** or download the source code:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install dependencies**:
   ```bash
   pip install tkcalendar
   ```

3. **Run the application**:
   ```bash
   python todo_manager.py
   ```

---

## Usage

1. **Add a Task**:
   - Enter the task name in the "Task" field.
   - Select a date using the calendar widget.
   - Set the time using the hour and minute spinboxes.
   - Click "Add Task" to save the task.

2. **Delete a Task**:
   - Select a task from the listbox.
   - Click "Delete Task" to remove it.

3. **Timer Alerts**:
   - When the set time is reached, a pop-up notification and sound alert will remind you of the task.

4. **Real-Time Display**:
   - The current time and countdown for active timers are displayed at the top of the window.

---

## Code Overview

### Key Functions

- **`check_timers()`**: Periodically checks active timers and triggers alerts when the time is up.
- **`update_current_time()`**: Updates the current time display every second.
- **`trigger_timer(task)`**: Displays a pop-up notification and plays a sound alert for the given task.
- **`add_task()`**: Adds a new task with a specified date and time.
- **`delete_task()`**: Deletes the selected task from the list.

### GUI Components

- **Task Entry**: Input field for task names.
- **Date Picker**: Calendar widget for selecting dates.
- **Time Spinboxes**: Spinboxes for selecting hours and minutes.
- **Task Listbox**: Displays all added tasks with their respective times.
- **Timer and Current Time Labels**: Show the countdown and current time.

---

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspired by productivity tools and user feedback to create a simple yet effective task manager.
- Special thanks to the `tkinter` and `tkcalendar` libraries for enabling the GUI and date selection features.

---

**Stay organized and never miss a deadline with the To-Do List Manager with Timers!**
