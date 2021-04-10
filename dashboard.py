from tkinter import *
from PIL import Image, ImageTk
import datetime as dt
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class Dashboard:

    #This is a constructor:
    def __init__(self, filterdDf):

        self.filterdDf = filterdDf

        root =Tk()
        root.title('Dashboard')
        root.geometry('1300x1000')
        root.resizable(False, False)

        frame = Frame(root, width=1000, height=680)
        frame.configure(background="gray28")
        frame.pack(fill=BOTH, expand=True)

        #TODO: Place a pie chart in the left side of the dashboard

        frameChartsLT = Frame(root)
        frameChartsLT.pack()

        fig = Figure()  # create a figure object
        ax = fig.add_subplot(111)  # add an Axes to the figure

        ax.pie(filterdDf[('Sum', '')], radius=1, shadow=True)

        chart1 = FigureCanvasTkAgg(fig, frameChartsLT)
        chart1.get_tk_widget().pack()

        #TODO: Place a table in the right side of the dashboard

        total_rows = len(filterdDf)
        print(total_rows)

        total_columns = len(filterdDf.columns)
        print(total_columns)



        #Saving charts for testing

        fig, ax = plt.subplots()
        plt.pie(filterdDf[('Sum', '')])

        # plt.show()

        plt.savefig('test.png')
        filterdDf.to_excel('filtered_df.xlsx')

        root.mainloop()




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