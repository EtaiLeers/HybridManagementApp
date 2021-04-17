from tkinter import *
from tkinter import ttk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import datetime as dt
import time


def normalize(value, max, min):
    v = (value - min) / (max - min) * (10 - 1) + 1
    return round(v)


def recommend(score):
    if score in range(6, 9):
        return 'Recommended'
    elif score in range(9, 11):
        return 'Highly Recommended'
    else:
        return 'Not related'


app_dict = {
    "Waterfall": ['Critical path analysis',
                  'Presenting the whole picture [End to end]',
                  'Focus on project stages',
                  'Emphasis on documentation',
                  'Detailed requirements specification',
                  'Progress control by earned value management',
                  'Hierarchical organizational structure',
                  'Formal communication',
                  'High-level planning'],
    "Agile": ['Sprint Retrospective',
              'Daily stand-up meetings',
              'Working system from day one',
              'Co-management: Customer and supplier cooperation',
              'Multi-disciplinary teams',
              'Self-organizing teams',
              'Progress control by burn down chart',
              'Rapid and flexible response to change',
              'Informal communication'],
    "TOC": ['Buffer Management',
            'Focus on critical chain on critical resources',
            'Sequential work - No multitasking',
            "Forecast project's bottlenecks & constraints",
            'Focus resources on the projects main constraint']
}

methods_dict = {
    "Waterfall": 0,
    "Agile": 0,
    "TOC": 0
}

#TODO: Add Logo


class Dashboard:

    def __init__(self, filterdDf):

        self.filterdDf = filterdDf

        root =Tk()
        root.title('Dashboard')
        root.geometry('1300x690')
        root.resizable(False, False)

        frame = Frame(root, width=1100, height=690)
        frame.configure(background="gray28")
        frame.pack(fill=BOTH, expand=True)

        header = Label(root, bg="gray28", fg="white", pady=3, font=("Helvetica", 26),
                       text='Hybrid management - system recommendations:')
        header.place(x=30, y=20)

        w = Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}",
                  bg="gray28", fg="white", pady=3, font=("Helvetica", 15))
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

        bottom_header = Label(root, bg="gray28", fg="white", pady=3, font=("Helvetica", 15),
                              text='Hybrid Management - where Agile, TOC and waterfall meet together')
        bottom_header.place(x=360, y=650)

        frameChartsLT = Frame(root)
        # frameChartsLT.pack(side='left', fill='y')
        frameChartsLT.place(x=-100, y=100)
        # frameChartsLT.configure(background="gray28")

        fig = Figure()  # create a figure object
        fig.set_facecolor('#474747')  # The color of the background
        ax = fig.add_subplot(111)  # add an Axes to the figure

        chart1 = FigureCanvasTkAgg(fig, frameChartsLT)
        chart1.get_tk_widget().pack()

        max_value = max(filterdDf[('Sum', '')])
        min_value = min(filterdDf[('Sum', '')])

        filterdDf[('Normalized sum', '')] = filterdDf['Sum'].apply(lambda x: normalize(x, max_value, min_value))

        filterdDf[('Recommendation Level', '')] = filterdDf[('Normalized sum', '')].apply(recommend)

        condition = filterdDf[('Recommendation Level', '')] != 'Not related'
        filterdDf = filterdDf[condition]

        rows = len(filterdDf)

        tree = ttk.Treeview(root, columns=(1, 2), height=rows, show="headings")
        tree.pack(side='left')
        tree.place(x=700, y=150)

        #Add some style:
        style = ttk.Style()

        style.theme_use("clam")


        style.configure("Treeview",
                        background="silver",
                        foreground="black",
                        rowheight=55,
                        fieldbackground="silver")

        #Change selected color:
        style.map("Treeview",
                  background=[('selected', 'green')])

        #TODO: Change font size in the table
        #TODO: Change the color of the rows according to the method type

        tree.heading("#0", text="Label", anchor=W)
        tree.heading("#1", text="Approach", anchor=CENTER)
        tree.heading("#2", text="Recommendation", anchor=CENTER)

        # tree['columns'] = ("Approach", "Recommendation")

        tree.column("#0", width=120, minwidth=25)
        tree.column("#1", width=300, minwidth=25, anchor=W)
        tree.column("#2", width=150, minwidth=25, anchor=CENTER)

        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')

        tree.configure(yscrollcommand=scroll.set)

        for i in range(rows):
            tree.insert(parent='', index='end', values=(filterdDf[('Approaches', 'All')].iloc[i],
                                           filterdDf[('Recommendation Level', '')].iloc[i]))

        methods = []

        for app in filterdDf[('Approaches', 'All')]:
            for key in app_dict:
                if app in app_dict[key]:
                    methods_dict[key] += 1
                    methods.append(key)

        filterdDf[('Methods', '')] = methods

        print(methods_dict.values())

        #TODO: Make the pie view look more 3D
        #TODO: Add below the percentage the methods names

        colors = ["lightskyblue", "turquoise", "deepskyblue"]
        ax.pie(methods_dict.values(), radius=1, autopct='%1.1f%%', shadow=True, colors=colors)
        labels = ['Waterfall', 'Agile', 'TOC']
        patches, texts = plt.pie(methods_dict.values(), colors=colors, shadow=True, startangle=90)
        ax.legend(patches, labels, loc="best")

        fig, ax = plt.subplots()

        # Saving charts for testing

        # plt.savefig('test.png')
        # ax.pie(methods_dict.values(), radius=1, autopct='%0.2f%%', shadow=False).savefig('Pie_test.png')

        filterdDf.to_excel('filtered_df2.xlsx')

        root.mainloop()

# df = pd.read_excel('filtered_df.xlsx', header=[0,1])
# dash = Dashboard(df)