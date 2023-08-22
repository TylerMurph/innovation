from tkinter import *

def click_function():

    day = enter_sv1.get()
    month = enter_sv2.get()
    year = enter_sv3.get()
    date.set(day + "/" + month + "/" + year)


my_window = Tk()

enter_sv1 = StringVar()
enter_sv2 = StringVar()
enter_sv3 = StringVar()
date = StringVar()

label1 = Label(my_window, text="Please Insert A Date!")
label1.grid(row=0, column=0)

entry1 = Entry(my_window, textvariable=enter_sv1)
entry1.grid(row=1, column=0)
entry2 = Entry(my_window, textvariable=enter_sv2)
entry2.grid(row=1, column=1)
entry3 = Entry(my_window, textvariable=enter_sv3)
entry3.grid(row=1, column=2)
button1 = Button(my_window, text="Confirm", command=click_function)
button1.grid(row=2, column=1)

label2 = Label(my_window, textvariable=date)
label2.grid(row=3, column=1)

my_window.mainloop()