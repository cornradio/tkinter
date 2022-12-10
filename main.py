import tkinter as tk
from tkinter import ttk

# Define the function to be called when the button is clicked
def on_button_click():
    # Increment the click count and update the label text
    global click_count
    click_count += 1
    label.config(text="Button clicks: {}".format(click_count))

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create a button and set its command
button = tk.Button(root, text="Click me!", command=on_button_click,fg="green")
button.pack()

# Create a label to display the button's click count
label = tk.Label(root, text="Button clicks: 0", bg="blue", fg="white")
label.pack()



# Set the initial click count to 0
click_count = 0

# Start the main loop
root.mainloop()
