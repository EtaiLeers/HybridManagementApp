from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def create_img(filename):
    img = Image.open(filename)
    img.thumbnail((100, 100))
    p_img = ImageTk.PhotoImage(img)
    return p_img


root = Tk()
root.geometry("500x200")

data = [["val1", "val2"],
         ["asd1", "asd2"],
         ["bbb1", "bbb3"],
         ["ccc1", "ccc3"],
         ["ddd1", "ddd3"],
         ["eee1", "eee3"]]


frame = Frame(root)
frame.pack()

image2 = create_img('Capture.JPG')
img2 = Label(root, image=image2)
img2.image = image2
img2.place(x=15, y=15)

tree = ttk.Treeview(frame, columns=(1, 2), height=5, show="headings")
tree.pack(side='left')

tree.heading(1, text="Column 1")
tree.heading(2, text="Column 2")

tree.column(1, width=100)
tree.column(2, width=100)

# Add some style:
style = ttk.Style()

style.theme_use("clam")

style.configure("Treeview",
                background="silver",
                foreground="black",
                rowheight=55,
                fieldbackground="silver")

# Change selected color:
style.map("Treeview",
          background=[('selected', 'green')])


scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side='right', fill='y')

tree.configure(yscrollcommand=scroll.set)

for val in data:
    tree.insert('', 'end', values=(val[0], val[1]))

root.mainloop()