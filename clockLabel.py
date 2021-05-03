import time
from tkinter import *

class Clock:

    def __init__(self, root):
        self.root = root

        self.clock_label = Label(self.root, bg="gray28", fg="white", pady=3, font=("Helvetica", 15))
        self.now = time.strftime("%H:%M:%S")
        self.clock_label.configure(text=self.now)
        self.updateTime()
        self.clock_label.place(x=1135, y=40)

    def updateTime(self):
        self.now = time.strftime("%H:%M:%S")
        self.clock_label.configure(text=self.now)
        self.root.after(20,self.updateTime)

# root = Tk()
# root.geometry('1300x690')
# Clock(root)
# root.mainloop()
