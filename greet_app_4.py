import tkinter as tk
from tkinter import ttk

# To enable High DPI
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()


def greet():
    print(f"Hello {user_name.get() or 'World'}")


# Decide the Layout
"""
    We will have the two frame one for the name and other for buttons. Hence creating that.
"""
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
button_frame = ttk.Frame(root, padding=(20, 10))

# pack it
input_frame.pack(fill="both")
button_frame.pack(fill="both")

user_name = tk.StringVar()
name_label = ttk.Label(input_frame, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

# adding a widget/button
green_button = ttk.Button(button_frame, text="Greet", command=greet)
green_button.pack(side="left", fill='x', expand=True)

quit_button = ttk.Button(button_frame, text="Quit", command=root.destroy)
quit_button.pack(side="right", fill='x', expand=True)

root.mainloop()
