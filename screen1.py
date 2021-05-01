from screen2 import printMenu2

from tkinter import * 

def f1():    

    root = Tk()

    root.title("Hotel_Management_Sys")

    root.geometry('550x500')

    root.configure(bg = 'grey')

    label = Label(root, text ="♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦ WELCOME TO HOTEL RASVED ♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦")
    label.grid(row = 1, column = 1, padx=0, pady=20)

    btn = Button(root, text = 'Book Your Room!', bd = '5', command = printMenu2)
    btn.grid(row = 3, column = 1, padx=0, pady=20)

    btn1 = Button(root, text = 'Booking Details', bd = '5', command = root.destroy)
    btn1.grid(row = 5, column = 1, padx=0, pady=20)

    btn2 = Button(root, text = 'Exit', bd = '5', command = root.destroy)
    btn2.grid(row = 7, column = 1, padx=0, pady=20)

    root.mainloop()