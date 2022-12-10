import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Tree View")

# Create a Treeview widget
tree = ttk.Treeview(root)

# Add some items to the tree
tree.insert("", 0, "item1", text="Item 1")
tree.insert("", 1, "item2", text="Item 2")
tree.insert("item2", 0, "subitem1", text="Subitem 1")
tree.pack()

# Start the main loop
root.mainloop()
