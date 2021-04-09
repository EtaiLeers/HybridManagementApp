from tkinter import *
import time


root = Tk()

root.title('Main Menu')
root.geometry('1300x690')
root.resizable(False, False)

frame = Frame(root, width=1000, height=680)
frame.configure(background="gray28")
frame.pack(fill=BOTH, expand=True)

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

root.mainloop()