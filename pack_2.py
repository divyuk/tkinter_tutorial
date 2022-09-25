import tkinter as tk

root = tk.Tk()

root.title("My first app")

tk.Label(root, text="Label 1", background="yellow", foreground='red').pack(side="left", expand=True)
tk.Label(root, text="Label 2", background="black", foreground='white').pack(side="top", fill="both", expand=True)
tk.Label(root, text="Label 3", background="blue", foreground='pink').pack(side="left", expand=True)
root.mainloop()
