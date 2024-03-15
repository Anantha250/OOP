from tkinter import *
import ttkbootstrap as ttk
from datetime import date
from ttkbootstrap.scrolled import ScrolledFrame

root = ttk.Window(themename='minty')
root.title("Frame")
root.geometry('1600x900')

def speak():
    my_label.config(text=f"You typed : {PromotioncodeEntry.get()}")


promotioncode = ttk.Frame(root, bootstyle="light")
promotioncode.pack(pady=5)


PromotioncodeEntry = ttk.Entry(promotioncode, bootstyle="success", 
                     font=("Helvetica",18),
                     foreground='blue',width = 20)
PromotioncodeEntry.pack(pady=5, padx=5)


my_button = ttk.Button(promotioncode, text="CONFRIM CODE", bootstyle="dark", command=speak)
my_button.pack(pady=5, padx=5)

my_label = ttk.Label(promotioncode, text = "")
my_label.pack(pady=2)

my_button = ttk.Button(root, text="CONFRIM ORDER", bootstyle="dark")
my_button.pack(pady=5, padx=5)


root.mainloop()

