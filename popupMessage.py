import tkinter as tk
import tkinter.ttk as ttk


def popupmsg(msg):
    popup = tk.Tk()
    label = ttk.Label(popup, text=msg, wraplength=580, justify=tk.LEFT)
    popup.title("Message from system")
    label.config(font=("Courier", 16))
    label.pack()
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack(side=tk.BOTTOM)
    popup.wm_attributes("-topmost", 1)
    popup.geometry("600x500")
    popup.pack_propagate(0)
    tk.mainloop()