from tkinter import *
import ttkbootstrap as ttk
from datetime import date,datetime
import requests
from PIL import Image, ImageTk
import time
from tkinter import filedialog
import tkinter as tk
from ttkbootstrap import Style, Label, Entry, Button

root = ttk.Window(themename="minty")
root.title("DKUB WATERPARK")
root.geometry("1920x1080")

member_id = 0

def set_user_id(user_id):
    global member_id
    member_id = user_id
    return member_id

def get_member_info(member_id):
    get_member_detail(member_id)
    show_page(4,frame_home_member)

def get_booking_his():
    booking_his()
    show_page(12, frame_view_member)

def get_order(member_id): ### สร้างมาลอง เดะลบ
    show_page(1,frame_home_member)
    get_order_detail(member_id)
    get_order_detail_total(member_id)

API_ENDPOINT3 = "http://127.0.0.1:8000/subscription"
API_ENDPOINT1 = "http://127.0.0.1:8000/login"

image_path = "6963703.jpg"  # Provide the path to your image file
image_path2 ="Bank.jpg"
image_path3 ="DKUB_logo.jpg"
image_path4 ="Design3.png"
image_path5 = "2.png"
image_path6 = "waterpark.png"
image_path7 = "water.png"
image_path8 = "background.png"
image = Image.open(image_path)
image2 = Image.open(image_path2)
image3 = Image.open(image_path3)
image4 = Image.open(image_path4)
image5 = Image.open(image_path5)
image_waterpark_home = Image.open(image_path6)
image_waterpark_register = Image.open(image_path7)
image_booking_his = Image.open(image_path8)
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
resized_image6 = image_waterpark_home.resize((1920, 1080), Image.BICUBIC)  # Adjust the size as needed
image_waterpark_home = ImageTk.PhotoImage(resized_image6)
resized_image7 = image_waterpark_register.resize((1920, 1080), Image.BICUBIC)  # Adjust the size as needed
image_waterpark_register = ImageTk.PhotoImage(resized_image7)
resized_image8 = image_booking_his.resize((1920, 1080), Image.BICUBIC)  # Adjust the size as needed
background_image = ImageTk.PhotoImage(resized_image8)




# สร้างตัวแปร global สำหรับแสดงข้อมูล
name_label = None
email_label = None
telephone_label = None
date_of_visit_label = None

frame_home = ttk.Frame(root)
frame_order = ttk.Frame(root)
frame_order_detail_member = ttk.Frame(root)
frame_home_1 = ttk.Frame(root)
frame_view_member = ttk.Frame(root)
frame_card_payment = ttk.Frame(root)
frame_bank_payment = ttk.Frame(root)
frame_payment_success = ttk.Frame(root)
frame_login = ttk.Frame(root)
frame_register = ttk.Frame(root)
frame_home_member = ttk.Frame(root)
frame_view_booking_his = ttk.Frame(root)

def set_user_id(user_id):
    global member_id
    member_id = user_id
    return member_id

def log_out():
    set_user_id(0)
    print(member_id)
    show_page(3,frame_home_member)



############################################################################################################

def show_page_home(page):
    if page == 8:
        frame_home_1.pack(fill="both", expand=True)
    
    
show_page_home(8)


def show_page(page, current_frame):
    current_frame.pack_forget()  # ซ่อน frame ปัจจุบัน

    if page == 1:
        frame_order_detail_member.pack(fill="both", expand=True)

    if page == 2:
        frame_order.pack()

    if page == 3:
        frame_home_1.pack(fill="both", expand=True)

    if page == 4:
        frame_view_member.pack(fill="both", expand=True)
    
    if page == 5:
        frame_card_payment.pack(fill="both", expand=True)
    
    if page == 6:
        frame_bank_payment.pack(fill="both", expand=True)

    if page == 7:
        frame_payment_success.pack(fill="both", expand=True)
    
    if page == 9:
        frame_login.pack(fill="both", expand=True)
    
    if page == 10:
        frame_register.pack(fill="both", expand=True)
    
    if page == 11:
        frame_home_member.pack(fill="both", expand=True)
    
    if page == 12:
        frame_view_booking_his.pack(fill="both", expand=True)
    
    if page == 13:
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
    print(member_id)
    print(response.json())
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

            order_label = ttk.Label(
                Order_detail_frame,
                text=f"Item Name: {name},  Amount: {amount},     Price: {price},       Subtotal: {subtotal}",
                font=("Helvetica", 14),
                bootstyle="dark",
            )
            order_label.place(x=50, y=100, relwidth=1, relheight=1)

        name_label.config(text=f"Name: {data['member']['name']}")
        email_label.config(text=f"Email: {data['member']['email']}")
        telephone_label.config(text=f"Telephone: {data['member']['phone_no']}")
        date_of_visit_label.config(text=f"Date of Visit: {order['visit_date']}")
        booking_id.config(text=f"Booking id: {data['booking']['booking_id']}")
        total_price_bank.config(text=f"Total Price:{order_total}")
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

    # สร้าง Label สำหรับแสดงข้อมูล
    

# Contact Detail

Contact_Image = ttk.Label(frame_order_detail_member, image=image5)
Contact_Image.place(x=0, y=0, relwidth=1, relheight=1)

Contact_Detail_Frame = ttk.Frame(frame_order_detail_member)
Contact_Detail_Frame.pack(pady=120, ipadx=10)

contrat_label = ttk.Label(
    frame_order_detail_member, text="Contact Detail", font=("Helvetica", 25),foreground= "green"
)
contrat_label.pack(pady=5, padx=5)


name_label = ttk.Label(
    frame_order_detail_member, text="Name :", font=("Helvetica", 14)
)
name_label.pack(pady=5, padx=5)

email_label = ttk.Label(
    frame_order_detail_member, text="Email :", font=("Helvetica", 14)
)
email_label.pack(pady=5, padx=5)

telephone_label = ttk.Label(
    frame_order_detail_member, text="Telephone :", font=("Helvetica", 14)
)
telephone_label.pack(pady=5, padx=5)

date_of_visit_label = ttk.Label(
    frame_order_detail_member,
    text="Date of Visit :",
    font=("Helvetica", 14)
)
date_of_visit_label.pack(pady=5, padx=5)

# Order Detail
Order_detail = ttk.Label(
    frame_order_detail_member, text="Order Detail", font=("Helvetica", 25), foreground="green"
)
Order_detail.pack(pady=10)

Order_detail_frame = ttk.Frame(frame_order_detail_member)
Order_detail_frame.pack(pady=10)

Order_detail_frame1 = ttk.Frame(frame_order_detail_member)
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

button1 = ttk.Button(Order_detail_frame1, image=image, command=lambda: show_page(5,frame_order_detail_member))
button1.pack(side="left", pady=10, padx=10)

button2 = ttk.Button(Order_detail_frame1, image=image2, command=lambda: show_page(6,frame_order_detail_member))
button2.pack(side="right", pady=10, padx=10,ipadx=1)

Button_frame = ttk.Frame(frame_order_detail_member)
Button_frame.pack(pady=10)

cancel_order3 = ttk.Button(Button_frame, text="BACK", command=lambda: show_page(11, frame_order_detail_member))
cancel_order3.pack(side="bottom", pady=10, padx=1)

################################################################################################################################


def get_member_detail(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_member_info"
    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        Member_name_view.config(text=f"Name: {data['name']}")
        Email_view.config(text=f"Email: {data['email']}")
        telephone_view.config(text=f"Telephone: {data['phone_no']}")
    else:
        print("Error_view_member")

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

cancel_order3 = ttk.Button(Member_detail_frame, text="VIEWORDERHISTORY", bootstyle="dark", command=lambda: get_booking_his())
cancel_order3.pack(pady=20, padx=2, ipadx=1)

cancel_order3 = ttk.Button(Member_detail_frame, text="BACK", bootstyle="dark", command=lambda: show_page(11, frame_view_member))
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
         return data["booking_id"]
    else:
        print("Error:", response.text)


# card_image = ttk.Label(frame_card_payment, image=image_waterpark_home)
# card_image.place(x=0, y=0, relwidth=1, relheight=1)

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
    payment_success(card_payment(member_id))

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






##############################################################################################################################















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
         return data
    else:
        print("Error:", response.text)


Dkub = ttk.Label(frame_bank_payment, text = "DKUB CO.,LTD.", font=("Helvetica",18), bootstyle="info")
Dkub.pack(pady=2)

booking_detail_frame = ttk.Frame(frame_bank_payment, bootstyle="light")
booking_detail_frame.pack(pady=2)

booking_id = ttk.Label(booking_detail_frame, text = "Booking id :", font=("Helvetica",14), bootstyle="dark")
booking_id.pack(pady=2,padx=2)

total_price_bank = ttk.Label(booking_detail_frame, text = "Total Price :", font=("Helvetica",14), bootstyle="dark")
total_price_bank.pack(pady=2,padx=2)

bank_detail_frame = ttk.Frame(frame_bank_payment, bootstyle="light")
bank_detail_frame.pack(pady=10)

my_label = ttk.Label(bank_detail_frame, text = "ATM/KIOSK", font=("Helvetica",14), bootstyle="PRIMARY")
my_label.pack(pady=5)

def click_bind(e):
        my_label.config(text=f"You Clinked on {bank_combo.get()}!")

banks = ['Kasikorn Bank','SCB','KrungThai Bank','KrungSri Bank','TMB BANK','UOB','Bangkok Bank']

bank_combo = ttk.Combobox(bank_detail_frame, bootstyle="info", values=banks)
bank_combo.pack(pady=5)

Global_Card = ttk.Label(bank_detail_frame, text = "Bank Number", font=("Helvetica",12), bootstyle="info")
Global_Card.pack(pady=2)

Bank_entry = ttk.Entry(bank_detail_frame, bootstyle="success",
                     font=("Helvetica",12),
                     foreground='blue',width = 20)
Bank_entry.pack(pady=5, padx=5)

def CONTINUE_PAYMENT():
    bank_payment(member_id)
    show_page(13,frame_bank_payment)
    

continue_payment = ttk.Button(bank_detail_frame, text="CONTINUE PAYMENT", bootstyle="dark",command=lambda : CONTINUE_PAYMENT()) 
continue_payment.pack(pady=2, padx=2,ipadx=1)

cancel_order = ttk.Button(bank_detail_frame, text="CANCEL", bootstyle="dark",command=lambda: show_page(1,frame_bank_payment)) #command=?)
cancel_order.pack(pady=2, padx=2,ipadx=1)



#############################################################################################################################
    
def login():
        
        email_l = email_entry_login.get()
        password_l = password_entry_login.get()
        payload = {
            "email": email_l,
            "password": password_l
        }
        response = requests.post(API_ENDPOINT1, json=payload)
        if email_l== ""  or password_l== "":
            result_label_login.config(text="Please fill all")
        elif response.json().get("Result") != "Email or password is incorrect.":
            member_id=set_user_id(response.json().get("Result"))
            result_label_login.config(text="Login successful")
            print(member_id)
            show_page(11,frame_login)
        else:
            result_label_login.config(text="Incorrect username or password")


login_Image = ttk.Label(frame_login, image=image_waterpark_register)
login_Image.place(relwidth=1, relheight=1)

login_detail_frame = ttk.Frame(frame_login, bootstyle="light")
login_detail_frame.place(relx=0.5, rely=0.4, anchor=ttk.CENTER)

to_register_frame = ttk.Frame(frame_login)
to_register_frame.place(relx=0.5, rely=0.54, anchor=ttk.CENTER)

x=2

message_label_login = ttk.Label(login_detail_frame, text="Log in",font = ("Arial", 12, "bold"))
message_label_login.grid(row=x-2, columnspan=2)

blank_label = ttk.Label(login_detail_frame, text="")
blank_label.grid(row=x-1, columnspan=2)

email_label_login = ttk.Label(login_detail_frame, text="Email : ")
email_label_login.grid(row=x+0, column=0,sticky='w')

email_entry_login = ttk.Entry(login_detail_frame)
email_entry_login.grid(row=x+0, column=1, padx=10, pady=5,)

password_label_login = ttk.Label(login_detail_frame, text="Password : ")
password_label_login.grid(row=x+1, column=0,sticky='w')

password_entry_login = ttk.Entry(login_detail_frame, show="*")
password_entry_login.grid(row=x+1, column=1, padx=10, pady=5)

blank_label = ttk.Label(login_detail_frame, text="")
blank_label.grid(row=x+2, columnspan=2)

# สร้างปุ่มเข้าสู่ระบบ
login_button = ttk.Button(login_detail_frame, text="sign in", command=login)
login_button.grid(row=x+3, columnspan=2, padx=10, pady=5)

    # สร้าง Label สำหรับผลลัพธ์
result_label_login = ttk.Label(login_detail_frame, text="")
result_label_login.grid(row=x+4, columnspan=2, padx=10, pady=5)

be_member_button = ttk.Button(to_register_frame, text="register",command=lambda: show_page(10,frame_login))
be_member_button.grid(row=10, columnspan=2)
    
home_button = ttk.Button(frame_login, text="Home", command= lambda :show_page(3,frame_login),width=10,padding=10)
home_button.grid(row=0,column=0)




############################################################################################################################

############################################################################################################################
     
def become_member():
        
        name = name_entry.get()
        email = email_entry.get()
        phone_no = phone_no_entry.get()
        
        date_str = birthday.entry.get()
        try:
            datetime.strptime(date_str, '%m/%d/%Y')  # ตรวจสอบว่าสามารถแปลงวันที่เป็นรูปแบบที่ถูกต้องหรือไม่
        except ValueError:
            result_label_register.config(text="Incorrect date format", foreground="red")
            return
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")# แปลงสตริงเป็นวัตถุ datetime
        birth_day =  date_obj.strftime("%Y-%m-%d")
        
        password = password_entry.get()
        
        
        
        payload = {
            "name": name,
            "email": email,
            "phone_no": phone_no,
            "birthday": birth_day,
            "password": password
        }
        #print("Becoming a member...")
        
        
            
        response = requests.post(API_ENDPOINT3, json=payload)
        if name== "" or email== "" or phone_no== "" or birth_day== "" or password== "":
            result_label_register.config(text="Please fill in compete information", foreground="red")
            
        elif response.json().get("Result") ==  'Membership registration completed.':
            result_label_register.config(text="Membership registration completed.",foreground="black")
            name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            phone_no_entry.delete(0, tk.END)
            birthday.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            #login_page()
        else :
            result_label_register.config(text=response.json().get("Result"),foreground="red")
            print(response.json().get("Result") )
        print(response.json().get("Result") )


Contact_Image1 = ttk.Label(frame_register, image=image_waterpark_register)
Contact_Image1.place(x=0, y=0, relwidth=1, relheight=1)


register_detail_frame = ttk.Frame(frame_register, bootstyle="light")
register_detail_frame.pack(padx= 10,pady =100, anchor=ttk.CENTER)

name_label4_register = Label(register_detail_frame, text="Name:")
name_label4_register.grid(row=0, column=0, padx=10, pady=5,sticky='w')

name_entry = Entry(register_detail_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5,sticky="news")

    # สร้าง Label และ Entry สำหรับกรอกอีเมล
email_label_register = Label(register_detail_frame, text="Email:")
email_label_register.grid(row=1, column=0, padx=10, pady=5,sticky='w')

email_entry = Entry(register_detail_frame)
email_entry.grid(row=1, column=1, padx=10, pady=5,sticky="news")

phone_no_label = Label(register_detail_frame, text="Phone Number:")
phone_no_label.grid(row=2, column=0, padx=10, pady=5 ,sticky='w')

phone_no_entry = Entry(register_detail_frame)
phone_no_entry.grid(row=2, column=1, padx=10, pady=5,sticky="news")

birthday_label = Label(register_detail_frame, text="Birthday:")
birthday_label.grid(row=3, column=0, padx=10, pady=5,sticky= 'w')

birthday = ttk.DateEntry(register_detail_frame, bootstyle="danger", startdate=date.today())
birthday.grid(row=3, column=1, padx=10, pady=5,sticky="news")

password_label = Label(register_detail_frame, text="Password:")
password_label.grid(row=4, column=0, padx=10, pady=5,sticky='w')

password_entry = Entry(register_detail_frame)
password_entry.grid(row=4, column=1, padx=10, pady=5,sticky="news")


    # สร้างปุ่ม "Become a Member"
become_member_button = Button(register_detail_frame, text="Become a Member", command=become_member)
become_member_button.grid(row=5, columnspan=2, padx=10, pady=5)

result_label_register = ttk.Label(register_detail_frame, text="")
result_label_register.grid(row=6, columnspan=2)
    
home_button = ttk.Button(Contact_Image1, text="Home", command=lambda :show_page(3,frame_register),width=10,padding=10)
home_button.grid(row=0,column=0)


##############################################################################################################################

width_botton = 76
c=0
pading_button=13

home_member = ttk.Label(frame_home_member, image=image_waterpark_home)
home_member.place(relwidth=1, relheight=1)

home_button = ttk.Button(frame_home_member, text="Home", command=lambda: show_page(11,frame_home_member),width=width_botton,padding=pading_button)
home_button.grid(row=0,column=c)

service_button = ttk.Button(frame_home_member, text="Service", command=lambda: get_order(member_id),width=width_botton,padding=pading_button)
service_button.grid(row=0,column=c+1)

login_button = ttk.Button(frame_home_member, text="info", command=lambda: get_member_info(member_id),width=width_botton,padding=pading_button)
login_button.grid(row=0,column=c+2)

register_button = ttk.Button(frame_home_member, text="Log out", command=log_out,width=width_botton,padding=pading_button)
register_button.grid(row=0,column=c+3)
    
print(f"Member :{member_id}")














##############################################################################################################################

############################################################################################################################


    
width_botton = 76
c=0
pading_button=12
    
home_image = ttk.Label(frame_home_1, image=image_waterpark_home)
home_image.place(x=0, y=0, relwidth=1, relheight=1)
    
home_button = ttk.Button(frame_home_1, text="Home", command= lambda :show_page(11,frame_home_1),width=width_botton,padding=pading_button)
home_button.grid(row=0,column=c)
    
service_button = ttk.Button(frame_home_1, text="Service", command= lambda :show_page(1,frame_home_1),width=width_botton,padding=pading_button)
service_button.grid(row=0,column=c+1)
    
login_button = ttk.Button(frame_home_1, text="Log in", command= lambda :show_page(9,frame_home_1),width=width_botton,padding=pading_button)
login_button.grid(row=0,column=c+2)
    
register_button = ttk.Button(frame_home_1, text="Register", command= lambda :show_page(10,frame_home_1),width=width_botton,padding=pading_button)
register_button.grid(row=0,column=c+3)

print(f"Home :{member_id}")

#############################################################################################

x_size, y_size = 1920, 1080

def get_all_services(member_id=""):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/services"
    if not member_id:
        API_ENDPOINT = "http://127.0.0.1:8000/services"
    req = requests.get(API_ENDPOINT)
    
    if req.status_code != 200:
        return "error"
    
    data = req.json()
    for key, val in data.items():
        print(key, val)

def get_show_all_booking(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{str(member_id)}/show_all_booking"
    req = requests.get(API_ENDPOINT)
    
    if req.status_code != 200:
        return "error"
    
    return req.json()

def download(member_id, booking_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{(member_id)}/finish_booking/{(booking_id)}"
    req = requests.get(API_ENDPOINT, stream=True)
    
    try:
        print(req.json())
    except:
        print(req)
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not save_path:
            return
        
        req.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in req.iter_content(chunk_size=8192):
                file.write(chunk)

def booking_his():

    booking = get_show_all_booking(member_id)
    

    # canvas = Canvas(root, width=x_size, height=y_size)
    #background_image = PhotoImage(file="background.png")
    # canvas.create_image(0, 0, anchor=NW, image=background_image)
    # canvas.pack()
    # Load your background image
    
    booking_frame = Frame(frame_view_booking_his)
    booking_frame.pack()
    label = ttk.Label(booking_frame, image=background_image)
    label.pack()

    # tab = ttk.Label(booking_frame, text="   ",padding=14, width=250, background='#009658')
    # tab.place(x=0,y=0)
    home_button = tk.Button(frame_view_booking_his, 
                bg='#ffffff',
                relief='flat',
                text='Home',
                width=20,
                command=lambda : show_page(4,frame_view_booking_his))
    home_button.place(x=x_size*0.02, y=16)
    for i in range(len(booking)):
        # Labels
        line = ttk.Label(booking_frame, text="___________________________________________________________________________________", font=("Helvetica", 15), background="#CDEDF4")
        l1 = ttk.Label(booking_frame, text=f"{str(booking[i]['booking_id'])}", font=("Helvetica", 15), background="#CDEDF4")
        l2 = ttk.Label(booking_frame, text=f"{str(booking[i]['visit_date'])}", font=("Helvetica", 15), background="#CDEDF4")
        b = ttk.Button(booking_frame, text="Download", bootstyle="success outline",padding="10 5",  # Adjust padding as needed
        command=lambda: download(member_id, booking[i]["booking_id"]))
        
        # Positioning using place
        line.place(x=x_size*0.5, y=228 + i * 40, anchor = CENTER)
        l1.place(x=x_size*0.3, y=220 + i * 40, anchor = CENTER)
        l2.place(x=x_size*0.5, y=220 + i * 40, anchor = CENTER)
        b.place(x=x_size*0.71, y=220 + i * 40, anchor = CENTER)









#####################################################################################################

def payment_success(booking_id):
    show_page(13,frame_card_payment)
    payment_success_frame = Frame(frame_payment_success)
    payment_success_frame.pack()
    label = ttk.Label(payment_success_frame, image=background_image)
    label.pack()


    home_button = tk.Button(frame_payment_success, 
        bg='#ffffff',
        relief='flat',
        text='Home',
        width=20,
        command=lambda : show_page(4,frame_payment_success))
    home_button.place(x=x_size*0.02, y=16)

    name_label = ttk.Label(
    frame_payment_success, text="PAYMENT SUCCESS :", font=("Helvetica", 14)
    )
    name_label.pack(pady=5, padx=5)


    b = ttk.Button(payment_success_frame, text="Download", bootstyle="success outline",padding="10 5",  # Adjust padding as needed
    command=lambda: download(member_id, booking_id))


    b.place(x=x_size*0.71, y=220, anchor = CENTER)






############################################################################################################################




# get_order_detail(member_id)

# get_order_detail_total(member_id)
get_member_detail(member_id)



root.mainloop()