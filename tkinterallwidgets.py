import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("All Widgets")

# Create a button and set its command
button = tk.Button(root, text="Click me!")  # command=on_button_click
button.pack()

# Create a checkbutton
checkbutton = tk.Checkbutton(root, text="Check me!")
checkbutton.pack()

# Create a radiobutton
radiobutton1 = tk.Radiobutton(root, text="Option 1")
radiobutton1.pack()
radiobutton2 = tk.Radiobutton(root, text="Option 2")
radiobutton2.pack()

# Create a listbox
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.pack()

# Create an entry field
entry = tk.Entry(root)
entry.pack()

# Create a label to display the button's click count
label = tk.Label(root, text="Button clicks: 0")
label.pack()

# Define the function to be called when the button is clicked
def on_button_click():
    # Increment the click count and update the label text
    global click_count
    click_count += 1
    label.config(text="Button clicks: {}".format(click_count))

# Set the initial click count to 0
click_count = 0

# Start the main loop
root.mainloop()
