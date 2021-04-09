from tkinter import *
from PIL import Image, ImageTk
import datetime as dt
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt


class Dashboard:

    #This is a constructor:
    def __init__(self, filterdDf):

        self.filterdDf = filterdDf

        root =Tk()
        root.title('Dashboard')
        root.geometry('1300x690')
        root.resizable(False, False)

        frame = Frame(root, width=1000, height=680)
        frame.configure(background="gray28")
        frame.pack(fill=BOTH, expand=True)

        #TODO: Continue from here:

        #print(filterdDf)
        #Check

        fig, ax = plt.subplots()
        plt.pie(filterdDf[('Sum', '')])

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