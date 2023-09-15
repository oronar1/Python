from email.message import EmailMessage
from smtplib import SMTP
import os
import requests
from tkinter import messagebox


def send_mail(message_to_send):
    message = EmailMessage()
    message['Subject'] = "AMAZON LOW PRICE"
    message['From'] = os.environ['SENDER_MAIL']
    message['To'] = os.environ['RECEIVER_MAIL']
    message.set_content(message_to_send)

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.environ['SENDER_MAIL'], password=os.environ['PASSWORD'])
        connection.sendmail(from_addr=os.environ['SENDER_MAIL'],
                            to_addrs= os.environ['RECEIVER_MAIL'],
                            msg=message_to_send)

        messagebox.showinfo(title="Successfully", message="Email has been sent successfully!!!")


def internet():
    try:
        requests.get("https://amazon.com/")
    except requests.exceptions.ConnectionError:
        return False
    else:
        return True
