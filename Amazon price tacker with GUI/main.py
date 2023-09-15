from tkinter import *
from add_url_to_file import add_url
from track_all_url_prices import track_prices
from send_mail import send_mail

def clear_gui():
    url_entry.delete(0, END)
    price_entry.delete(0, END)
    url_entry.focus()

def add_url_to_json_file():
    if add_url(url_entry.get(), price_entry.get()):
        clear_gui()


def track_all_prices():
    message_to_send = track_prices()
    if message_to_send:
        send_mail(message_to_send)

################# GUI #################
window = Tk()
# Window settings
window.title("AMAZON PRICE")
window.geometry("1200x600+0+0")
window.resizable(False, False)
canvas = Canvas(width=1200, height=600)
canvas.place(x=0, y=0)

img = PhotoImage(file="img.png")
canvas.create_image(650, 350, image=img)
COLOR_A = "#b07304"
COLOR_B = "#e19606"
COLOR_C = "#654104"
COLOR_D = "#322716"
COLOR_E = "#c28407"
COLOR_G = "#b97b04"
# AMAZON PRICE LABEL
company_label = Label(text="AMAZON PRICE TRACKER", font=("Arial", 36, "bold"), background=COLOR_C, foreground="white")
company_label.place(x=300, y=10)
# GET AMAZON URL
url_label = Label(text="Enter Amazon URL", background=COLOR_B, foreground=COLOR_C, font=("Arial", 22, "bold"))
url_label.place(x=240, y=130)
url_entry = Entry(width=45, font=("Arial", 22), highlightthickness=2, highlightbackground=COLOR_C,
                  highlightcolor=COLOR_C)
url_entry.grid(row=0, column=1, padx=200, pady=20)
url_entry.place(x=240, y=180)
url_entry.focus()
# PRICE
price_label = Label(text="Enter Your Lowest Price", background=COLOR_B, foreground=COLOR_C, font=("Arial", 22, "bold"))
price_label.place(x=240, y=230)
price_entry = Entry(width=21, font=("Arial", 22), highlightthickness=2, highlightbackground=COLOR_C,
                    highlightcolor=COLOR_C)
price_entry.place(x=240, y=277)
# BUTTONS
cheap_flights_button = Button(text="ADD URL TO TRACK PRICE", background=COLOR_E, foreground=COLOR_D,
                              font=("Arial", 15, "bold"), command=add_url_to_json_file)
cheap_flights_button.place(x=644, y=277, width=325)
cheap_flights_in_6_month_button = Button(text="TRACK ALL CHEAP PRICES", background=COLOR_G, foreground=COLOR_D,
                                         font=("Arial", 15, "bold"), command=track_all_prices)
cheap_flights_in_6_month_button.place(x=644, y=347, width=325)
window.mainloop()
