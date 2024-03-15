from tkinter import *
import ttkbootstrap as ttk
from datetime import date
import requests
from PIL import Image, ImageTk
import time
from tkinter import filedialog

root = ttk.Window(themename="minty")
root.title("DKUB WATERPARK")
root.geometry("1920x1080")

member_id = 100001

image_path = "6963703.jpg"  # Provide the path to your image file
image_path2 ="Bank.jpg"
image_path3 ="DKUB_logo.jpg"
image_path4 ="Design3.png"
image_path5 = "2.png"
image = Image.open(image_path)
image2 = Image.open(image_path2)
image3 = Image.open(image_path3)
image4 = Image.open(image_path4)
image5 = Image.open(image_path5)
resized_image = image.resize((120, 120), Image.BICUBIC)  # Adjust the size as needed
image = ImageTk.PhotoImage(resized_image)
resized_image2 = image2.resize((120, 120), Image.BICUBIC)  # Adjust the size as needed
image2 = ImageTk.PhotoImage(resized_image2)
resized_image3 = image3.resize((1000, 150), Image.BICUBIC)  # Adjust the size as needed
image3 = ImageTk.PhotoImage(resized_image3)
resized_image4 = image4.resize((1920, 1080), Image.BICUBIC)  # Adjust the size as needed
image4 = ImageTk.PhotoImage(resized_image4)
resized_image5 = image5.resize((1920, 1080), Image.BICUBIC)  # Adjust the size as needed
image5 = ImageTk.PhotoImage(resized_image5)


# สร้างตัวแปร global สำหรับแสดงข้อมูล
name_label = None
email_label = None
telephone_label = None
date_of_visit_label = None

frame_home = ttk.Frame(root)
frame_order = ttk.Frame(root)
frame_home_1 = ttk.Frame(root)
frame_view_member = ttk.Frame(root)
frame_card_payment = ttk.Frame(root)
frame_bank_payment = ttk.Frame(root)
frame_payment_success = ttk.Frame(root)


############################################################################################################
def show_page_1(page):

    if page == 4:
        frame_home_1.pack()


show_page_1(4)


def show_page(page, current_frame):
    current_frame.pack_forget()  # ซ่อน frame ปัจจุบัน

    if page == 1:
        frame_home.pack(fill="both", expand=True)

    if page == 2:
        frame_order.pack()

    if page == 3:
        frame_home_1.pack()

    if page == 4:
        frame_view_member.pack(fill="both", expand=True)
    
    if page == 5:
        frame_card_payment.pack(fill="both", expand=True)
    
    if page == 6:
        frame_bank_payment.pack(fill="both", expand=True)

    if page == 7:
        frame_payment_success.pack(fill="both", expand=True)

############################################################################################################


def coupon_use(member_id,date):
    promocode = PromotioncodeEntry.get()
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/services/{date}"
    response = requests.put(
        API_ENDPOINT, json={"code": promocode}
    )

    if response.status_code == 200:
         data = response.json()  # แก้ไขตรงนี้
         print("Response Data:", data)
    else:
        print("Error:", response.text)

promotioncode = ttk.Frame(frame_order, bootstyle="light")
promotioncode.pack(pady=5)

PromotioncodeEntry = ttk.Entry(
    promotioncode,
    bootstyle="success",
    font=("Helvetica", 18),
    foreground="blue",
    width=20,
)
PromotioncodeEntry.pack(pady=5, padx=5)

confirm_button = ttk.Button(frame_order, text="Confirm Code", command=lambda: coupon_function())
confirm_button.pack()

def coupon_function():
    coupon_use(member_id,"2024-03-12")


my_label = ttk.Label(promotioncode, text="")
my_label.pack(pady=2)

my_button = ttk.Button(frame_order, text="CONFRIM ORDER", bootstyle="dark")
my_button.pack(pady=5, padx=5)

cancel_order3 = ttk.Button(
    frame_order,
    text="BACK",
    bootstyle="dark",
    command=lambda: show_page(3, frame_order),
)
cancel_order3.pack(pady=20, padx=2, ipadx=1)


############################################################################################################


def get_order_detail(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_confirm"
    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        booking = data["booking"]
        order = booking["order"]
        order_total = order["total"]


        for order_detail in order["order_detail"]:
            item_name = order_detail["item"]
            name = item_name["name"]
            price = item_name["price"]
            subtotal = order_detail["total_price"]
            amount = order_detail["amount"]
            if "size" in item_name:
                size = item_name["size"]
            else:
                size = "None"

            order_label = ttk.Label(
                Order_detail_frame,
                text=f"Item Name: {name},    Size: {size},    Amount: {amount},     Price: {price},       Subtotal: {subtotal}",
                font=("Helvetica", 14),
                bootstyle="dark",
            )
            order_label.pack(pady=5, padx=10, ipadx=10)

        name_label.config(text=f"Name: {data['member']['name']}")
        email_label.config(text=f"Email: {data['member']['email']}")
        telephone_label.config(text=f"Telephone: {data['member']['phone_no']}")
        date_of_visit_label.config(text=f"Date of Visit: {order['visit_date']}")
        booking_id.config(text=f"Booking id: {data['booking']['booking_id']}")
        total_price.config(text=f"Total Price:{order_total}")
        booking_id2.config(text=f"Booking id: {data['booking']['booking_id']}")
        total_price2.config(text=f"Total Price:{order_total}")
    else:
        print("Error")


############################################################################################################



def get_order_detail_total(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_confirm"
    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        booking = data["booking"]
        order = booking["order"]
        order_total = order["total"]
        order_discount = order["discount"]
        Grand_Total.config(text=f"Grand Total: {order_total}")
        Discount.config(text=f"Discount:{order_discount}")
    else:
        print("Error")

    root.after(10000, lambda: get_order_detail_total(member_id))

    # สร้าง Label สำหรับแสดงข้อมูล
    

# Contact Detail

Contact_Image = ttk.Label(frame_home, image=image5)
Contact_Image.place(x=0, y=0, relwidth=1, relheight=1)

Contact_Detail_Frame = ttk.Frame(frame_home)
Contact_Detail_Frame.pack(pady=120, ipadx=10)

contrat_label = ttk.Label(
    frame_home, text="Contact Detail", font=("Helvetica", 25),foreground= "green"
)
contrat_label.pack(pady=5, padx=5)


name_label = ttk.Label(
    frame_home, text="Name :", font=("Helvetica", 14)
)
name_label.pack(pady=5, padx=5)

email_label = ttk.Label(
    frame_home, text="Email :", font=("Helvetica", 14)
)
email_label.pack(pady=5, padx=5)

telephone_label = ttk.Label(
    frame_home, text="Telephone :", font=("Helvetica", 14)
)
telephone_label.pack(pady=5, padx=5)

date_of_visit_label = ttk.Label(
    frame_home,
    text="Date of Visit :",
    font=("Helvetica", 14)
)
date_of_visit_label.pack(pady=5, padx=5)

# Order Detail
Order_detail = ttk.Label(
    frame_home, text="Order Detail", font=("Helvetica", 25), foreground="green"
)
Order_detail.pack(pady=10)

Order_detail_frame = ttk.Frame(frame_home)
Order_detail_frame.pack(pady=10)

Order_detail_frame1 = ttk.Frame(frame_home)
Order_detail_frame1.pack(pady=10)

Grand_Total = ttk.Label(
    Order_detail_frame1, text="Grand Total :", font=("Helvetica", 14)
)
Grand_Total.pack(pady=5, padx=5)

Discount = ttk.Label(
    Order_detail_frame1, text="Discount :", font=("Helvetica", 14)
)
Discount.pack(pady=5, padx=5)

# Payment Method
Payment_Method = ttk.Label(
    Order_detail_frame1, text="Payment Method", font=("Helvetica", 25), foreground="green"
)
Payment_Method.pack(pady=10)

button1 = ttk.Button(Order_detail_frame1, image=image, command=lambda: show_page(5,frame_home))
button1.pack(side="left", pady=10, padx=10)

button2 = ttk.Button(Order_detail_frame1, image=image2, command=lambda: show_page(6,frame_home))
button2.pack(side="right", pady=10, padx=10,ipadx=1)

Button_frame = ttk.Frame(frame_home)
Button_frame.pack(pady=10)

cancel_order3 = ttk.Button(Button_frame, text="BACK", command=lambda: show_page(3, frame_home))
cancel_order3.pack(side="bottom", pady=10, padx=1)

################################################################################################################################


def get_member_detail(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_confirm"
    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        booking = data["booking"]
        order = booking["order"]

        Member_name_view.config(text=f"Name: {data['member']['name']}")
        Email_view.config(text=f"Email: {data['member']['email']}")
        telephone_view.config(text=f"Telephone: {data['member']['phone_no']}")
    else:
        print("Error")

Contact_Image = ttk.Label(frame_view_member, image=image4)
Contact_Image.place(x=0, y=0, relwidth=1, relheight=1)

Contact_Detail = ttk.Label(frame_view_member, text="Member Detail", font=("Helvetica", 45), foreground="green")
Contact_Detail.place(relx=0.5, rely=0.4, anchor="center")

Member_detail_frame = ttk.Frame(frame_view_member,bootstyle = "light")
Member_detail_frame.place(relx=0.5, rely=0.6, anchor="center")

Member_name_view = ttk.Label(Member_detail_frame, text="Name :", font=("Helvetica", 30))
Member_name_view.pack(pady=10, padx=10, ipadx=10)

Email_view = ttk.Label(Member_detail_frame, text="Email :", font=("Helvetica", 30))
Email_view.pack(pady=10, padx=10, ipadx=10)

telephone_view = ttk.Label(Member_detail_frame, text="Telephone :", font=("Helvetica", 30))
telephone_view.pack(pady=10, padx=10, ipadx=10)

cancel_order3 = ttk.Button(Member_detail_frame, text="VIEWORDERHISTORY", bootstyle="dark", command=lambda: show_page(3, frame_view_member))
cancel_order3.pack(pady=20, padx=2, ipadx=1)

cancel_order3 = ttk.Button(Member_detail_frame, text="BACK", bootstyle="dark", command=lambda: show_page(3, frame_view_member))
cancel_order3.pack(pady=20, padx=2, ipadx=1)


################################################################################################################################


def card_payment(member_id):
    card_no = Card_number.get()
    card_pin = Card_pin.get()
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_payment/card"
    response = requests.put(
        API_ENDPOINT, json={"card_no": card_no,"card_pin" :card_pin }
    )

    if response.status_code  == 200:
         data = response.json()  # แก้ไขตรงนี้
         print("Response Data:", data)
    else:
        print("Error:", response.text)


Dkub = ttk.Label(frame_card_payment, text = "DKUB CO.,LTD.", font=("Helvetica",18), bootstyle="info")
Dkub.pack(pady=2)

booking_detail_frame = ttk.Frame(frame_card_payment)
booking_detail_frame.pack(pady=2)

booking_id2 = ttk.Label(booking_detail_frame, text = "Booking id :", font=("Helvetica",14), bootstyle="dark")
booking_id2.pack(pady=2,padx=2)

total_price2 = ttk.Label(booking_detail_frame, text = "Total Price :", font=("Helvetica",14), bootstyle="dark")
total_price2.pack(pady=2,padx=2)

Global_Card = ttk.Label(frame_card_payment, text = "GLOBAL CARD", font=("Helvetica",14), bootstyle="info")
Global_Card.pack(pady=10)

card_detail_frame = ttk.Frame(frame_card_payment, bootstyle="light")
card_detail_frame.pack(pady=2)

Global_Card = ttk.Label(card_detail_frame, text = "Card Number", font=("Helvetica",14), bootstyle="info")
Global_Card.pack(pady=2)

def card_payment_click():
    card_payment(member_id)

Card_number = ttk.Entry(card_detail_frame, bootstyle="success",
                     font=("Helvetica",12),
                     foreground='blue',width = 20)
Card_number.pack(pady=5, padx=5)

Global_Card = ttk.Label(card_detail_frame, text = "Card pin", font=("Helvetica",12), bootstyle="info")
Global_Card.pack(pady=2)

Card_pin = ttk.Entry(card_detail_frame, bootstyle="success", 
                     font=("Helvetica",12),
                     foreground='blue',width = 20)
Card_pin.pack(pady=5, padx=5)

continue_payment = ttk.Button(card_detail_frame, text="CONTINUE PAYMENT", bootstyle="dark",command= lambda: card_payment_click())
continue_payment.pack(pady=2, padx=2,ipadx=1)

cancel = ttk.Button(card_detail_frame, text="CANCEL", bootstyle="dark",command=lambda : show_page(1,frame_card_payment)) #command=?)
cancel.pack(pady=2, padx=2,ipadx=1)









############################################################################################################################


def bank_payment(member_id):
    bank_no = Bank_entry.get()
    bank_name1 = bank_combo.get()
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_payment/bank"
    response = requests.put(
        API_ENDPOINT, json={"account_no": int(bank_no), "bank_name": bank_name1}
    )

    if response.status_code  == 200:    
         data = response.json()  # แก้ไขตรงนี้
         print("Response Data:", data)
    else:
        print("Error:", response.text)


Dkub = ttk.Label(frame_bank_payment, text = "DKUB CO.,LTD.", font=("Helvetica",18), bootstyle="info")
Dkub.pack(pady=2)

booking_detail_frame = ttk.Frame(frame_bank_payment, bootstyle="light")
booking_detail_frame.pack(pady=2)

booking_id = ttk.Label(booking_detail_frame, text = "Booking id :", font=("Helvetica",14), bootstyle="dark")
booking_id.pack(pady=2,padx=2)

total_price = ttk.Label(booking_detail_frame, text = "Total Price :", font=("Helvetica",14), bootstyle="dark")
total_price.pack(pady=2,padx=2)

card_detail_frame = ttk.Frame(frame_bank_payment, bootstyle="light")
card_detail_frame.pack(pady=10)

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

def CONTINUE_PAYMENT():
    bank_payment(member_id)
    show_page(7,frame_bank_payment)
    

continue_payment = ttk.Button(card_detail_frame, text="CONTINUE PAYMENT", bootstyle="dark",command=lambda : CONTINUE_PAYMENT()) 
continue_payment.pack(pady=2, padx=2,ipadx=1)

cancel_order = ttk.Button(card_detail_frame, text="CANCEL", bootstyle="dark",command=lambda: show_page(1,frame_bank_payment)) #command=?)
cancel_order.pack(pady=2, padx=2,ipadx=1)






############################################################################################################################























############################################################################################################################



def get_all_services(member_id = ""):
    api = f"http://127.0.0.1:8000/{member_id}/services"
    if member_id == "":
        api = f"http://127.0.0.1:8000/services"
    req = requests.get(api)
    if req.status_code != 200:
        return "error"
    data = req.json()
    for key, val in data.items():
        print(key, val)

def get_show_all_booking(member_id):
    api = f"http://127.0.0.1:8000/{str(member_id)}/show_all_booking"
    req = requests.get(api)
    if req.status_code != 200:
        return "error"
    return req.json()
    #api = f"http://127.0.0.1:8000/{member_id}/show_all_booking"
    
def download(member_id, booking_id):
    api = f"http://127.0.0.1:8000/{str(member_id)}/finish_booking/{(booking_id)}"
    req = requests.get(api, stream=True)
    try:
        print(req.json())
    except:
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not save_path:
            return
        req.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in req.iter_content(chunk_size=8192):
                file.write(chunk)

booking = get_show_all_booking(member_id)

print(booking)

for i in range(len(booking)):
    l1 = ttk.Label(frame_payment_success, 
                text=f"Booking ID : {(booking[i]['booking_id'])}",  
                bootstyle="info"
        )
    l2 = ttk.Label(frame_payment_success, 
                text=f"Date : {(booking[i]['visit_date']) }", 
                bootstyle="info"
        )
    b = ttk.Button(frame_payment_success, 
                text="Download", 
                bootstyle="success outline", 
                command=lambda: download(member_id, booking[i]["booking_id"])
        )
    l1.pack(side="left", padx=200)
    l2.pack(side="left", padx=200)
    b.pack(side="left", padx=200)
    


############################################################################################################################

get_order_detail("100001")

get_order_detail_total("100001")
get_member_detail("100001")


home = ttk.Button(
    frame_home_1,
    text="VIEW_ORDER_DETAIL",
    bootstyle="dark",
    command=lambda: show_page(1, frame_home_1),
)
home.pack(pady=20, padx=2, ipadx=1)

home2 = ttk.Button(
    frame_home_1,
    text="VIEW_COUPON_DETAIL",
    bootstyle="dark",
    command=lambda: show_page(2, frame_home_1),
)
home2.pack(pady=20, padx=2, ipadx=1)

home3 = ttk.Button(
    frame_home_1,
    text="VIEW_MEMBER_DETAIL",
    bootstyle="dark",
    command=lambda: show_page(4, frame_home_1),
)
home3.pack(pady=20, padx=2, ipadx=1)


root.mainloop()