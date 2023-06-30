from tkinter import *


def miles_2_km():
    print(input.get())
    mil=input.get()
    result = float(mil) * 1.609344
    numres_label.config(text=f"{result}")
    #return mil * 1.609344


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=100, height=100)
window.config(padx=15, pady=15)

#Label
eq_label = Label(text="Is equal to:", font=("Arial", 24, "bold"))
numres_label = Label(text="0", font=("Arial", 24, "bold"))
res1_label = Label(text="Miles", font=("Arial", 24, "bold"))
res_label = Label(text="Km", font=("Arial", 24, "bold"))

eq_label.grid(column=0, row=1)
numres_label.grid(column=1, row=1)
res1_label.grid(column=3, row=0)
res_label.grid(column=3, row=1)
eq_label.config(padx=20, pady=20)
numres_label.config(padx=20, pady=20)
res1_label.config(padx=20, pady=20)
res_label.config(padx=20, pady=20)

#Button
button = Button(text="Convert", command=miles_2_km)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
