from tkinter import *

choice_1 = 0

def butt_1():
    choice_1 * 0 + 1
    return choice_1

def butt_2():
    choice_1 * 0 + 2
    return choice_1

def printMenu2():

    choice_1 = 0

    root = Tk()

    root.title("Hotel_Management_Sys")

    root.geometry('550x500')

    root.configure(bg = 'grey')

    label = Label(root, text ="SELECT ROOM TYPE:")
    label.place(x = 220, y = 20)

    btn = Button(root, text = '1. AC', bd = '5', command = butt_1)
    btn.place(x = 250, y = 100)

    btn1 = Button(root, text = '2. Non-AC', bd = '5', command = butt_2)
    btn1.place(x = 237, y = 200)

    root.mainloop()
