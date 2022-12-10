import tkinter as tk
from tkinter import ttk
import os

# Define a function to recursively add the contents of a directory to the tree
def add_directory_to_tree(tree, path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            # Add the directory to the tree
            tree.insert(path, "end", item_path, text=item)
            # Recursively add the directory's contents to the tree
            add_directory_to_tree(tree, item_path)
        else:
            # Add the file to the tree
            tree.insert(path, "end", item_path, text=item)
# Create the main window
root = tk.Tk()
root.title("Tree View")
# Create a frame to hold the widget
# frame = tk.Frame(root)
# frame.grid(row=0, column=0)
# # Configure the grid to allow the widget to be resized
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)
# Create a Treeview widget
tree = ttk.Treeview(root)

# Add the files and directories on the desktop to the tree
desktop_path = "/Users/kasusa/Desktop"
for item in os.listdir(desktop_path):
    path = os.path.join(desktop_path, item)
    if os.path.isdir(path):
        # Add the directory to the tree
        tree.insert("", "end", path, text=item)
        # Recursively add the directory's contents to the tree
        add_directory_to_tree(tree, path)
    else:
        # Add the file to the tree
        tree.insert("", "end", path, text=item)

tree.pack(fill="both",expand=True)

# Start the main loop
root.mainloop()
