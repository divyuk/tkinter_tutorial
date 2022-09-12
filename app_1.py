import tkinter as tk
from tkinter import ttk  # allow more widget!! themed tkinter


def greet():
    print(f"Hello , {user_name.get() or 'World'}!")


root = tk.Tk()  # object of tkinter

user_name = tk.StringVar()
name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()  # As soon as the window opens the cursor blinks on the placeholder

# adding a widget/button
green_button = ttk.Button(root, text="Greet", command=greet)
green_button.pack(side="left")

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="right")

root.mainloop()  # It stops the current running program and enters the event loop of tkinter app.
