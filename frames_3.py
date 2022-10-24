"""
A frame is essentially a container to hold our widgets and in turn it can also become like a widget !
"""
import tkinter as tk

root = tk.Tk()  # this is the root container
main = tk.Frame(root)  # this is the main container placed on top of the root
main.pack(side="left", fill="both", expand=True)

# three labels
tk.Label(main, text="Label 1", bg="Red").pack(side="top", fill="both", expand=True)
tk.Label(main, text="Label 2", bg="blue").pack(side="top", fill="both", expand=True)
tk.Label(root, text="Label 3", bg="green").pack(side="left", fill="both", expand=True)

root.mainloop()
