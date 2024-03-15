from tkinter import *
import ttkbootstrap as ttk
from datetime import date
import requests

root = ttk.Window(themename='minty')
root.title("Frame")
root.geometry('1600x900')


Dkub = ttk.Label(root, text = "MEMBER INFO", font=("Helvetica",18), bootstyle="info")
Dkub.grid(row=1,column=100)

booking_detail_frame = ttk.Frame(root, bootstyle="light")
booking_detail_frame.grid(row=10,column=100)

name_label = ttk.Label(booking_detail_frame, text = "NAME:", font=("Helvetica",10), bootstyle="dark")
name_label.grid(row=10,column=100)

root.mainloop()