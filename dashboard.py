from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import datetime as dt
import time



class Dashboard:

    def __init__(self, filterdDf):

        self.filterdDf = filterdDf

        root =Tk()
        root.title('Dashboard')
        root.geometry('1300x690')
        root.resizable(False, False)

        frame = Frame(root, width=1300, height=690)
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

        bottom_header = Label(root, bg="gray28", fg="white", pady=3, font=("Helvetica", 15), text='Hybrid Management - where Agile, TOC and waterfall meet together')
        bottom_header.place(x=360, y=650)

        #TODO: Place a pie chart in the left side of the dashboard

        frameChartsLT = Frame(root)
        # frameChartsLT.pack(side='left', fill='y')
        frameChartsLT.place(x=90, y=180)
        frameChartsLT.configure(background="gray28")

        fig = Figure()  # create a figure object
        fig.set_facecolor('#474747')  # The color of the background
        ax = fig.add_subplot(111)  # add an Axes to the figure

        ax.pie(filterdDf[('Sum', '')], radius=1, autopct='%0.2f%%', shadow=False)

        chart1 = FigureCanvasTkAgg(fig, frameChartsLT)
        chart1.get_tk_widget().pack()

        #TODO: Place a table in the right side of the dashboard

        #_________________________________________________________________

        # data = [["val1", "val2"],
        #         ["asd1", "asd2"],
        #         ["bbb1", "bbb3"],
        #         ["ccc1", "ccc3"],
        #         ["ddd1", "ddd3"],
        #         ["eee1", "eee3"]]

        myData = filterdDf['Approaches'].values.tolist()

        print("____14/4____")
        print(myData)

        # print(filterdDf)

        # print(data.values.tolist())

        # print(filterdDf.loc[:, 'Approaches'])

        # data = filterdDf.loc[:, 'Approaches']

        # filterdDf.loc[:, 'Approaches'].to_excel('data.xlsx')

        rows = len(myData)

        # tree = ttk.Treeview(frame, columns=(1, 2), height=5, show="headings")
        tree = ttk.Treeview(frame, columns=1, height=rows, show="headings")
        tree.pack(side='left')
        tree.place(x=750, y=150)

        tree.heading(1, text="Approaches")
        # tree.heading(2, text="Column 2")

        tree.column(1, width=300)
        # tree.column(2, width=300)

        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')

        tree.configure(yscrollcommand=scroll.set)

        # for val in data:
        #     tree.insert('', 'end', values=(val[0], val[1]))

        for val in myData:
            tree.insert('', 'end', values=val)

        #_________________________________________________________________

        total_rows = len(filterdDf)
        # print(total_rows)

        total_columns = len(filterdDf.columns)
        # print(total_columns)

        #Saving charts for testing

        fig, ax = plt.subplots()
        plt.pie(filterdDf[('Sum', '')])

        plt.savefig('test.png')
        filterdDf.to_excel('filtered_df.xlsx')

        print('The Sums of rows:\n')
        print(filterdDf[('Sum', '')])

        root.mainloop()

        #_________________________________________________________________

'''
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
        "Agile":     ['Sprint Retrospective',
                      'Daily stand-up meetings',
                      'Working system from day one',
                      'Co-management: Customer and supplier cooperation',
                      'Multi-disciplinary teams',
                      'Self-organizing teams',
                      'Progress control by burn down chart',
                      'Rapid and flexible response to change',
                      'Informal communication'],
        "TOC":       ['Buffer Management',
                      'Throughput analysis',
                      'Focus on critical chain on critical resources',
                      'Sequential work - No multitasking',
                      'Forecast projects bottlenecks & constraints',
                      'Focus resources on the projects main constraint']
    }
'''