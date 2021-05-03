from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import datetime as dt
from dashboard import Dashboard
import dashboard
import time
from readExcel import readFromExcel

# global Budget, Commitment, Contract_Type, Customer_Type, Duration, Goals, Pace, Procedures_and_Regulations
# global Resources, Scope, Team_Availability, Team_Distribution, Team_Size, Uncertainty

# I created a dictionary outside of everything
var_dict = dict()


def create_image(filename):
    img = Image.open(filename)
    img.thumbnail((100, 100))
    p_img = ImageTk.PhotoImage(img)
    return p_img


def close_window():
    import sys
    sys.exit()


# TODO: Add Logo


class Input:
    Budget = {'Flexible', 'Variable', 'Fixed'}
    Commitment = {'High', 'Medium', 'Low'}
    Contract_Type = {'Cost Plus', 'Hybrid', 'Fixed Price'}
    Customer_Type = {'Market', 'Single External', 'Single Internal'}
    Duration = {'Long', 'Medium', 'Short'}
    Goals = {'Well defined', 'Estimated', 'Unclear'}
    Pace = {'Time critical', 'Fast', 'Regular'}
    Procedures_and_Regulations = {'None', 'Standart procedures', 'Highly structured'}
    Resources = {'Versatile', 'Standart', 'Unique expertise'}
    Scope = {'Modular', 'Multiple delivery units', 'Rigid'}
    Team_Availability = {'Fully', 'Partially', 'Limited'}
    Team_Distribution = {'Single-location', 'Multi-location', 'Global'}
    Team_Size = {'Small', 'Medium', 'Large'}
    Uncertainty = {'Ambiguous', 'Predictable', 'Highly predictable'}

    def __init__(self):

        self.root = Tk()
        self.root.title('Input window V1')
        self.root.geometry('1300x690')
        self.root.resizable(False, False)

        frame = Frame(self.root, width=1000, height=680)
        frame.configure(background="gray28")
        frame.pack(fill=BOTH, expand=True)

        # now = time.strftime("%H:%M:%S")
        # clock_label = Label(self.root, bg="gray28", fg="white", pady=3, font=("Helvetica", 15))
        #
        # def display_time():
        #     now = time.strftime("%H:%M:%S")
        #     clock_label.configure(text=now)
        #     self.root.after(20, display_time)
        #
        # display_time()
        #
        # clock_label.configure(text=now)
        # clock_label.place(x=1135, y=40)
        # clock_label.after(20, time)

        image2 = create_image('Capture.JPG')
        img2 = Label(image=image2)
        img2.image = image2
        img2.place(x=15, y=15)


        progress = Progressbar(self.root, orient=HORIZONTAL, length=300, mode='determinate')
        progress.place(x=500, y=15)

        # TODO: Fix the bug of the progress bar
        # TODO: Add exception pop up message for missing attributes

        def callback(*args):
            # Increment the progressbar's value by 7.1428%
            progress["value"] += 7.1428

        bottom_header = Label(self.root, bg="gray28", fg="white", pady=3,
                              font=("Helvetica", 30, 'underline'), text='Please fill the following attributes:')
        bottom_header.place(x=240, y=155)

        lbl1 = Label(self.root, bg="gray28", pady=1, text='Budget:', fg="cyan2", font=("Helvetica", 20))
        lbl1.place(x=240, y=225)

        lbl2 = Label(self.root, bg="gray28", pady=1, text='Commitment:', fg="cyan2", font=("Helvetica", 20))
        lbl2.place(x=240, y=265)

        lbl3 = Label(self.root, bg="gray28", pady=1, text='Contract Type:', fg="cyan2", font=("Helvetica", 20))
        lbl3.place(x=240, y=305)

        lbl4 = Label(self.root, bg="gray28", pady=1, text='Customer Type:', fg="cyan2", font=("Helvetica", 20))
        lbl4.place(x=240, y=345)

        lbl5 = Label(self.root, bg="gray28", pady=1, text='Duration:', fg="cyan2", font=("Helvetica", 20))
        lbl5.place(x=240, y=385)

        lbl6 = Label(self.root, bg="gray28", pady=1, text='Goals:', fg="cyan2", font=("Helvetica", 20))
        lbl6.place(x=240, y=425)

        lbl7 = Label(self.root, bg="gray28", pady=1, text='Pace:', fg="cyan2", font=("Helvetica", 20))
        lbl7.place(x=240, y=465)

        lbl8 = Label(self.root, bg="gray28", pady=1, text='Proc. and Regs:', fg="cyan2", font=("Helvetica", 20))
        lbl8.place(x=670, y=225)

        lbl9 = Label(self.root, bg="gray28", pady=1, text='Resources:', fg="cyan2", font=("Helvetica", 20))
        lbl9.place(x=670, y=265)

        lbl10 = Label(self.root, bg="gray28", pady=1, text='Scope:', fg="cyan2", font=("Helvetica", 20))
        lbl10.place(x=670, y=305)

        lbl11 = Label(self.root, bg="gray28", pady=1, text='Team Availability:', fg="cyan2", font=("Helvetica", 20))
        lbl11.place(x=670, y=345)

        lbl12 = Label(self.root, bg="gray28", pady=1, text='Team Distribution:', fg="cyan2", font=("Helvetica", 20))
        lbl12.place(x=670, y=385)

        lbl13 = Label(self.root, bg="gray28", pady=1, text='Team Size:', fg="cyan2", font=("Helvetica", 20))
        lbl13.place(x=670, y=425)

        lbl14 = Label(self.root, bg="gray28", pady=1, text='Uncertainty:', fg="cyan2", font=("Helvetica", 20))
        lbl14.place(x=670, y=465)

        # _____________________________________________

        var1 = StringVar(self.root)
        # var1.set("None") # default value
        pl1 = OptionMenu(self.root, var1, *self.Budget)
        # var1.trace_add('write', lambda *args: print(var1.get()))
        pl1.config(width=20, bg="GREEN", fg="white")
        pl1.place(x=470, y=230)

        var1.trace("w", callback)

        var2 = StringVar(self.root)
        pl2 = OptionMenu(self.root, var2, *self.Commitment)
        # var2.trace_add('write', lambda *args: print(var2.get()))
        pl2.config(width=20, bg="GREEN", fg="white")
        pl2.place(x=470, y=270)

        var2.trace("w", callback)

        var3 = StringVar(self.root)
        pl3 = OptionMenu(self.root, var3, *self.Contract_Type)
        # var3.trace_add('write', lambda *args: print(var3.get()))
        pl3.config(width=20, bg="GREEN", fg="white")
        pl3.place(x=470, y=310)

        var3.trace("w", callback)

        var4 = StringVar(self.root)
        pl4 = OptionMenu(self.root, var4, *self.Customer_Type)
        # var4.trace_add('write', lambda *args: print(var4.get()))
        pl4.config(width=20, bg="GREEN", fg="white")
        pl4.place(x=470, y=350)

        var4.trace("w", callback)

        var5 = StringVar(self.root)
        pl5 = OptionMenu(self.root, var5, *self.Duration)
        # var5.trace_add('write', lambda *args: print(var5.get()))
        pl5.config(width=20, bg="GREEN", fg="white")
        pl5.place(x=470, y=390)

        var5.trace("w", callback)

        var6 = StringVar(self.root)
        pl6 = OptionMenu(self.root, var6, *self.Goals)
        # var6.trace_add('write', lambda *args: print(var6.get()))
        pl6.config(width=20, bg="GREEN", fg="white")
        pl6.place(x=470, y=430)

        var6.trace("w", callback)

        var7 = StringVar(self.root)
        pl7 = OptionMenu(self.root, var7, *self.Pace)
        # var7.trace_add('write', lambda *args: print(var7.get()))
        pl7.config(width=20, bg="GREEN", fg="white")
        pl7.place(x=470, y=470)

        var7.trace("w", callback)

        var8 = StringVar(self.root)
        pl8 = OptionMenu(self.root, var8, *self.Procedures_and_Regulations)
        # var8.trace_add('write', lambda *args: print(var8.get()))
        pl8.config(width=20, bg="GREEN", fg="white")
        pl8.place(x=960, y=230)

        var8.trace("w", callback)

        var9 = StringVar(self.root)
        pl9 = OptionMenu(self.root, var9, *self.Resources)
        # var9.trace_add('write', lambda *args: print(var9.get()))
        pl9.config(width=20, bg="GREEN", fg="white")
        pl9.place(x=960, y=270)

        var9.trace("w", callback)

        var10 = StringVar(self.root)
        pl10 = OptionMenu(self.root, var10, *self.Scope)
        # var10.trace_add('write', lambda *args: print(var10.get()))
        pl10.config(width=20, bg="GREEN", fg="white")
        pl10.place(x=960, y=310)

        var10.trace("w", callback)

        var11 = StringVar(self.root)
        pl11 = OptionMenu(self.root, var11, *self.Team_Availability)
        # var11.trace_add('write', lambda *args: print(var11.get()))
        pl11.config(width=20, bg="GREEN", fg="white")
        pl11.place(x=960, y=350)

        var11.trace("w", callback)

        var12 = StringVar(self.root)
        pl12 = OptionMenu(self.root, var12, *self.Team_Distribution)
        # var12.trace_add('write', lambda *args: print(var12.get()))
        pl12.config(width=20, bg="GREEN", fg="white")
        pl12.place(x=960, y=390)

        var12.trace("w", callback)

        var13 = StringVar(self.root)
        pl13 = OptionMenu(self.root, var13, *self.Team_Size)
        # var13.trace_add('write', lambda *args: print(var13.get()))
        pl13.config(width=20, bg="GREEN", fg="white")
        pl13.place(x=960, y=430)

        var13.trace("w", callback)

        var14 = StringVar(self.root)
        pl14 = OptionMenu(self.root, var14, *self.Uncertainty)
        # var14.trace_add('write', lambda *args: print(var14.get()))
        pl14.config(width=20, bg="GREEN", fg="white")
        pl14.place(x=960, y=470)

        var14.trace("w", callback)

        # Going to variable defined at the beginning
        global var_dict
        var_dict = dict(Budget=var1,
                        Commitment=var2,
                        Contract_Type=var3,
                        Customer_Type=var4,
                        Duration=var5,
                        Goals=var6,
                        Pace=var7,
                        Procedures_and_Regulations=var8,
                        Resources=var9,
                        Scope=var10,
                        Team_Availability=var11,
                        Team_Distribution=var12,
                        Team_Size=var13,
                        Uncertainty=var14)

        # _____________________________________________

        bottom_header = Label(self.root, bg="gray28", fg="white", pady=3, font=("Helvetica", 15),
                              text='Hybrid Management - where Agile, TOC and waterfall meet together')
        bottom_header.place(x=360, y=650)

        # _____________________________________________

        # TODO: Replace between this lines: (Test)

        button1 = Button(self.root, text="GO Hybrid !", command=self.validatePickLists)
        # button1 = Button(self.root, text="Test", command=self.test)
        button1.config(width=25, bg="white")
        button1.place(x=600, y=590)

        # _____________________________________________

        w = Label(self.root, text=f"{dt.datetime.now():%a, %b %d %Y}",
                  bg="gray28", fg="white", pady=3, font=("Helvetica", 15))
        w.place(x=1100, y=15)

        self.root.mainloop()


    def validatePickLists(self):
        global var_dict
        validate_var_dict = {}

        # Doing iterations on my Dictionary so I can get the final values (After .get())

        for key in var_dict.keys():
            var = var_dict[key]
            validate_var_dict[key] = var.get()

        try:
            self.dashboard(validate_var_dict)
        except KeyError:
            messagebox.showerror('Error', 'Please...')


    def dashboard(self, validate_var_dict):
        filterdDf = readFromExcel(validate_var_dict)

        self.root.destroy()
        dashboardTk = Dashboard(filterdDf)

    # TODO: Delete function before submitting: (Debugging only)

    def test(self):
        global var_dict

        var_dict = dict(Budget="Fixed",
                        Commitment="Low",
                        Contract_Type="Hybrid",
                        Customer_Type="Market",
                        Duration="Long",
                        Goals="Unclear",
                        Pace="Fast",
                        Procedures_and_Regulations="None",
                        Resources="Standart",
                        Scope="Rigid",
                        Team_Availability="Fully",
                        Team_Distribution="Global",
                        Team_Size="Small",
                        Uncertainty="Predictable")


        filterdDf = readFromExcel(var_dict)
        self.root.destroy()
        Dashboard(filterdDf)


