from tkinter import *
from PIL import Image, ImageTk
# from login import Login, Register
from inputScreen import Input
from menu import MainMenu
import datetime as dt
import time
import pandas as pd

#TODO: Add Excel file with users credentials - Login + Register


def create_img(filename):
    img = Image.open(filename)
    img.thumbnail((100, 100))
    p_img = ImageTk.PhotoImage(img)
    return p_img


class MainWindow:

    def __init__(self):
        self.app = Tk()
        self.app.title('Hybrid Managment system V1')
        self.app.resizable(False, False)

        frame = Frame(self.app, width=1000, height=680)
        frame.configure(background="gray28")
        frame.pack(fill=BOTH, expand=True)

        image1 = create_img('login3.jpg')
        img = Label(frame, image=image1)
        img.image = image1
        img.place(x=450, y=150)

        image2 = create_img('Capture.JPG')
        img2 = Label(frame, image=image2)
        img2.image = image2
        img2.place(x=15, y=15)

        w = Label(self.app, text=f"{dt.datetime.now():%a, %b %d %Y}", bg="gray28", fg="white", pady=3, font=("Helvetica", 15))
        w.place(x=820, y=20)

        self.label = Label(self.app, bg="gray28", fg="white", pady=3, font=("Helvetica", 10), text='Forgot password?')
        self.label.place(x=445, y=440)

        self.label_username = Label(self.app, bg="gray28", fg="white", pady=3, font=("Helvetica", 12), text='User name:')
        self.label_username.place(x=400, y=300)

        self.label_password = Label(self.app, bg="gray28", fg="white", pady=3, font=("Helvetica", 12), text='Password:')
        self.label_password.place(x=400, y=350)

        self.usernameS = StringVar()
        self.passwordS = StringVar()

        self.usernameE = Entry(self.app, relief=FLAT, textvariable=self.usernameS)
        self.usernameE.place(x=490, y=305)

        print(self.usernameE)

        #self.login = Button(self.app, text='Login',pady=5, padx=30, command=login)
        self.login = Button(self.app, text='Login', pady=5, padx=30, command=menu)
        self.login.place(x=450, y=400)

        #TODO: Undo hiding to the following line in order to enable users registration:

        # self.register = Button(self.app, text='Register', pady=5, padx=20, command=register)
        # self.register.place(x=900, y=640)

        self.passwordE = Entry(self.app, show='*', relief=FLAT, textvariable=self.passwordS)
        self.passwordE.place(x=490, y=355)

        bottom_header = Label(self.app, bg="gray28", fg="white", pady=3, font=("Helvetica", 15), text=('Hybrid Management - where Agile, TOC and waterfall meet together'))
        bottom_header.place(x=200, y=630)

    def run(self):
        self.app.mainloop()
        self.app.display_time()


def menu():
    main.app.destroy()
    inputTk = MainMenu()
    inputTk.run()

#Go straight to the Input screen:

# def input():
#     main.app.destroy()
#     inputTk = Input()
#     inputTk.run()

# def register():
#     registerTk = Register()
#     registerTk.run()

# def login():
#     loginTk = Login()
#     loginTk.run()

main = MainWindow()
main.run()
