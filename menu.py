from tkinter import Tk, Frame, Label, BOTH, Button, messagebox
from PIL import Image, ImageTk
import datetime as dt
import time
from inputScreen import Input


def create_img(filename):
    img = Image.open(filename)
    img.thumbnail((100, 100))
    p_img = ImageTk.PhotoImage(img)
    return p_img


def message():
    messagebox.showinfo("Hybrid Management - Notification", "We're sorry, this functionality is not supported yet.")

#TODO: Add Username value in the upper left corner


class MainMenu:

    def __init__(self):

        self.root = Tk()
        self.root.title('Main Menu')
        self.root.geometry('1300x690')
        self.root.resizable(False, False)

        frame = Frame(self.root, width=1000, height=690)
        frame.configure(background="gray28")
        frame.pack(fill=BOTH, expand=True)

        w = Label(self.root, text=f"{dt.datetime.now():%a, %b %d %Y}", bg="gray28", fg="white", pady=3, font=("Helvetica", 15))
        w.place(x=1100, y=15)

        # now = time.strftime("%H:%M:%S")
        # clock_label = Label(self.root, bg="gray28", fg="white", pady=3, font=("Helvetica", 15))
        #
        # def display_time(root):
        #     now = time.strftime("%H:%M:%S")
        #     clock_label.configure(text=now)
        #     root.after(20, display_time)
        #
        # display_time(self.root)
        #
        # clock_label.configure(text=now)
        # clock_label.place(x=1135, y=40)
        # clock_label.after(20, time)

        image2 = create_img('Capture.JPG')
        img2 = Label(frame, image=image2)
        img2.image = image2
        img2.place(x=15, y=15)

        header = Label(self.root, bg="gray28", fg="white", pady=3, font=("Helvetica", 30), text='Main Menu:')
        header.place(x=540, y=155)

        button1 = Button(self.root, text="Insert New Project", command=self.input)
        button1.config(bg="aquamarine2", pady=10, padx=20, width=20, height=4)
        button1.place(x=350, y=320)

        button2 = Button(self.root, text="Projects Records", command=message)
        button2.config(bg="aquamarine2", pady=10, padx=20, width=20, height=4)
        button2.place(x=550, y=320)

        button3 = Button(self.root, text="Settings", command=message)
        button3.config(bg="aquamarine2", pady=10, padx=20, width=20, height=4)
        button3.place(x=750, y=320)

        bottom_header = Label(self.root, bg="gray28", fg="white", pady=3, font=("Helvetica", 15),
                              text='Hybrid Management - where Agile, TOC and waterfall meet together')
        bottom_header.place(x=360, y=650)

    def input(self):
        self.root.destroy()
        Input()