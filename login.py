from tkinter import *
from PIL import Image, ImageTk
import datetime as dt
import time
from tkinter import messagebox


def create_img(filename):
    img = Image.open(filename)
    img.thumbnail((100, 100))
    p_img = ImageTk.PhotoImage(img)
    return p_img


root = Tk()
root.title('Main Menu')
root.geometry('1300x690')
root.resizable(False, False)

frame = Frame(root, width=1000, height=690)
frame.configure(background="gray28")
frame.pack(fill=BOTH, expand=True)

w = Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}", bg="gray28", fg="white", pady=3, font=("Helvetica", 15))
w.place(x=1100, y=15)

now = time.strftime("%H:%M:%S")
clock_label = Label(root, bg="gray28", fg="white", pady=3, font=("Helvetica", 15))


def display_time():
    now = time.strftime("%H:%M:%S")
    clock_label.configure(text=now)
    root.after(20, display_time)


display_time()

clock_label.configure(text=now)
clock_label.place(x=1135, y=40)
clock_label.after(20, time)

image2 = create_img('Capture.JPG')
img2 = Label(frame, image=image2)
img2.image = image2
img2.place(x=15, y=15)

header = Label(root, bg="gray28", fg="white", pady=3, font=("Helvetica", 30), text='Login:')
header.place(x=540, y=155)


label_username = Label(root, bg="gray28", fg="white", pady=3, font=("Helvetica", 16), text='User name:')
label_username.place(x=400, y=300)

label_password = Label(root, bg="gray28", fg="white", pady=3, font=("Helvetica", 16), text='Password:')
label_password.place(x=400, y=350)

usernameS = StringVar()
passwordS = StringVar()

passwordE = Entry(root, show='*', relief=FLAT, textvariable=passwordS)
passwordE.place(x=520, y=360)

usernameE = Entry(root, relief=FLAT, textvariable=usernameS)
usernameE.place(x=520, y=310)

bottom_header = Label(root, bg="gray28", fg="white", pady=3, font=("Helvetica", 15),
                      text='Hybrid Management - where Agile, TOC and waterfall meet together')
bottom_header.place(x=360, y=650)

root.mainloop()

