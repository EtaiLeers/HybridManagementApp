from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from database import Database
from menu import MainMenu
import datetime as dt
# from clockLabel import Clock

db = Database()
db.createTable()

#TODO: Write Register function (Show stopper)
#TODO: Add Clock for all screens (Feature)

def create_img(filename):
    img = Image.open(filename)
    img.thumbnail((100, 100))
    p_img = ImageTk.PhotoImage(img)
    return p_img

class MainWindow:

    def __init__(self):
        self.root = Tk()
        self.root.title('Hybrid Management system V1')
        self.root.resizable(False, False)

        frame = Frame(self.root, width=1000, height=680)
        frame.configure(background="gray28")
        frame.pack(fill=BOTH, expand=True)

        image1 = create_img('Images/login3.jpg')
        img = Label(frame, image=image1)
        img.image = image1
        img.place(x=450, y=150)

        image2 = create_img('Images/Capture.JPG')
        img2 = Label(frame, image=image2)
        img2.image = image2
        img2.place(x=15, y=15)

        image3 = create_img('Images/about_test.JPG')
        img3 = Label(frame, image=image3)
        img3.image = image3
        img3.place(x=10, y=570)

        w = Label(self.root, text=f"{dt.datetime.now():%a, %b %d %Y}", bg="gray28", fg="white", pady=3, font=("Helvetica", 15))
        w.place(x=820, y=20)


        # self.now = time.strftime("%H:%M:%S")
        # clock_label = Label(self.root, bg="gray28", fg="white", pady=3, font=("Helvetica", 15))
        #
        # def display_time(root):
        #     now = time.strftime("%H:%M:%S")
        #     clock_label.configure(text=now)
        #     root.after(20, display_time)
        #
        # display_time(self.root)


        self.label = Label(self.root, bg="gray28", fg="cyan2", pady=3, font=("Helvetica", 8), text='Scan to read about us')
        self.label.place(x=5, y=550)

        self.label_username = Label(self.root, bg="gray28", fg="white", pady=3, font=("Helvetica", 12), text='User name:')
        self.label_username.place(x=400, y=300)

        self.label_password = Label(self.root, bg="gray28", fg="white", pady=3, font=("Helvetica", 12), text='Password:')
        self.label_password.place(x=400, y=350)

        self.usernameS = StringVar()
        self.passwordS = StringVar()

        self.passwordE = Entry(self.root, show='*', relief=FLAT, textvariable=self.passwordS)
        self.passwordE.place(x=490, y=355)

        self.usernameE = Entry(self.root, relief=FLAT, textvariable=self.usernameS)
        self.usernameE.place(x=490, y=305)

        print(self.usernameE)

        #TODO: Switch for testing (Direct to Menu) / Validate with Database (Test)

        self.login = Button(self.root, text='Login',pady=5, padx=30, command=self.validate)
        # self.login = Button(self.root, text='Login', pady=5, padx=30, command=menu)
        self.login.place(x=450, y=400)

        #TODO: Undo hiding to the following line in order to enable users registration (Test)

        self.register = Button(self.root, text='Register', pady=5, padx=20, command=self.register)
        self.register.place(x=900, y=640)

        bottom_header = Label(self.root, bg="gray28", fg="white", pady=3, font=("Helvetica", 15), text='Hybrid Management - where Agile, TOC and waterfall meet together')
        bottom_header.place(x=200, y=630)

        # Clock(self.root)

    def run(self):
        self.root.mainloop()


    def validate(self):
        data = self.usernameS.get()
        inputData = (self.usernameS.get(), self.passwordS.get(),)
        try:
            if db.validateData(data, inputData):
                messagebox.showinfo('Successful', 'Login Was Successful')
                menu(data)
            else:
                messagebox.showerror('Error', 'Wrong Credentials')
        except IndexError:
            messagebox.showerror('Error', 'Wrong Credentials')
        except ValueError:
            messagebox.showerror('Error', 'You must provide credentials')


    def register(self):
        r = Register()


class Register:

    def __init__(self):
        self.root =Tk()
        self.root.title('Register')
        self.root.geometry('500x380')
        self.root.resizable(False, False)
        self.root.configure(background="gray28")

        self.label = Label(self.root, bg="gray28", fg="cyan2", pady=5, font=("Helvetica", 16), text='Hybrid management system - registration window')
        self.label.place(x=10, y=5)

        self.label_username = Label(self.root, bg="gray28", fg="white", pady=3, font=("Helvetica", 12), text='User name:')
        self.label_username.place(x=125, y=120)

        self.label_password = Label(self.root, bg="gray28", fg="white", pady=3, font=("Helvetica", 12), text='Password:')
        self.label_password.place(x=125, y=180)

        self.usernameS = StringVar(self.root)
        self.passwordS = StringVar(self.root)

        self.usernameE = Entry(self.root, relief=FLAT, textvariable=self.usernameS)
        self.usernameE.place(x=225, y=125)

        self.passwordE = Entry(self.root, relief=FLAT, textvariable=self.passwordS)
        self.passwordE.place(x=225, y=185)

        self.register = Button(self.root, text='Add Me!', pady=5, padx=30, command=self.add)
        self.register.place(x=200, y=300)


    def add(self):
        data = self.usernameS.get()
        try:
            result = db.searchData(data)
            print(result)

            if result != 0:
                data = (self.usernameS.get(), self.passwordS.get())
                db.insertData(data)
                messagebox.showinfo('Successful', 'Username Was Added')
            else:
                messagebox.showwarning('Warning', 'Username already Exists')

            self.root.destroy()

        except ValueError:
            messagebox.showerror('Error','Invalid credentials')


def menu(username):
    main.root.destroy()
    menu_screen = MainMenu(username)

main = MainWindow()
main.run()