from tkinter import *
import ttkbootstrap as ttk
from datetime import date
import requests

root = ttk.Window(themename='minty')
root.title("Frame")
root.geometry('1600x900')


Dkub = ttk.Label(root, text = "DKUB CO.,LTD.", font=("Helvetica",18), bootstyle="info")
Dkub.pack(pady=2)

booking_detail_frame = ttk.Frame(root, bootstyle="light")
booking_detail_frame.pack(pady=2)

booking_id = ttk.Label(booking_detail_frame, text = "Booking id :", font=("Helvetica",7), bootstyle="dark")
booking_id.pack(pady=2,padx=2,ipadx=300)

total_price = ttk.Label(booking_detail_frame, text = "Total Price :", font=("Helvetica",7), bootstyle="dark")
total_price.pack(pady=2,padx=2,ipadx=300)

card_detail_frame = ttk.Frame(root, bootstyle="light")
card_detail_frame.pack(pady=2)

my_label = ttk.Label(card_detail_frame, text = "ATM/KIOSK", font=("Helvetica",14), bootstyle="PRIMARY")
my_label.pack(pady=5)

def click_bind(e):
        my_label.config(text=f"You Clinked on {bank_combo.get()}!")

banks = ['Kasikorn Bank','SCB','KrungThai Bank','KrungSri Bank','TMB BANK','UOB','Bangkok Bank']

bank_combo = ttk.Combobox(card_detail_frame, bootstyle="info", values=banks)
bank_combo.pack(pady=5)

Global_Card = ttk.Label(card_detail_frame, text = "Bank Number", font=("Helvetica",12), bootstyle="info")
Global_Card.pack(pady=2)

Bank_entry = ttk.Entry(card_detail_frame, bootstyle="success", 
                     font=("Helvetica",12),
                     foreground='blue',width = 20)
Bank_entry.pack(pady=5, padx=5)

continue_payment = ttk.Button(card_detail_frame, text="CONTINUE PAYMENT", bootstyle="dark") #command=?)
continue_payment.pack(pady=2, padx=2,ipadx=1)

cancel_order = ttk.Button(card_detail_frame, text="CANCEL", bootstyle="dark") #command=?)
cancel_order.pack(pady=2, padx=2,ipadx=1)

# telephone_label = ttk.Label(Contact_Detail_Frame, text = "Telephone :", font=("Helvetica",14), bootstyle="dark")
# telephone_label.pack(pady=10,padx=10,ipadx=280)

# date_of_visit_label = ttk.Label(Contact_Detail_Frame, text = "Date of Visit :", font=("Helvetica",14), bootstyle="dark")
# date_of_visit_label.pack(pady=10,padx=10,ipadx=275)

root.mainloop()