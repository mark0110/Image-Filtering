import tkinter as tk
import tkinter.ttk as ttk

def popupmsg(msg):
    popup = tk.Tk()
    label = ttk.Label(popup, text=msg, wraplength=500, justify=tk.LEFT)
    popup.title("Message from system")
    label.config(font=("Courier", 20))
    label.pack()
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.wm_attributes("-topmost", 1)
    popup.geometry("+400+200")
    tk.mainloop()