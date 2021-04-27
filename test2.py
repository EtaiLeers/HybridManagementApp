from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import time

from pandas._libs.reshape import explode


def create_img(filename):
    img = Image.open(filename)
    img.thumbnail((100, 100))
    p_img = ImageTk.PhotoImage(img)
    return p_img


class Dashboard:

    def __init__(self):

        root =Tk()
        root.title('Dashboard')
        root.geometry('1300x690')
        root.resizable(False, False)
        # root.configure(background="gray28")

        image2 = create_img('Capture.JPG')
        img2 = Label(root, image=image2)
        img2.image = image2
        img2.place(x=15, y=15)

        w = Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="gray28", pady=3, font=("Helvetica", 15))
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

        y = np.array([35, 25, 25, 15])
        mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
        mycolors = ["black", "hotpink", "b", "#4CAF50"]
        myexplode = [0.2, 0, 0, 0]
        plt.pie(y, labels=mylabels, colors=mycolors, explode = myexplode, shadow = True)
        plt.legend(title = "Four Fruits:")
        plt.show()
        explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = plt.subplots()
        ax1.pie(y, explode=explode, labels=mylabels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()


        bottom_header = Label(root, fg="white",bg="gray28", pady=3, font=("Helvetica", 15),
                              text='Hybrid Management - where Agile, TOC and waterfall meet together')
        bottom_header.place(x=360, y=650)

        root.mainloop()


test = Dashboard()