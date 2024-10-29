# Digital Clock 

This code creates a simple digital clock application using Tkinter, a GUI toolkit in Python. Here’s a summary of its main components:

## Components

- **Imports**: The code imports necessary modules from Tkinter and the `strftime` function from the time module.

- **Window Setup**: A main window (`root`) is created with a title "Clock" and a black background.

- **Time Function**: The `time` function fetches the current time in the format "HH:MM:SS AM/PM" and updates a label every second.

- **Date Function**: The `date` function retrieves the current date in the format "DD/Mon/YYYY" and updates a label every 24 hours.

- **Day Function**: The `day` function gets the current day of the week (e.g., Monday) and updates a label every 24 hours.

- **Labels**: Three labels are created to display the time, date, and day of the week, styled with specific fonts and colors.

- **Main Loop**: The `mainloop()` function starts the Tkinter event loop, allowing the window to remain open and responsive.

## Features

- Displays current time, date, and day.
- Customizable appearance.

## Requirements

- Python 3.x
- Tkinter (included with most Python installations)
