from tkinter import *
from tkinter.ttk import *
from person import Person
from log import Log


class Menu(Notebook):
    residentTab = None

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.residentTab = Frame()
        self.add(self.residentTab, text="Residents")
        self.pack()

    def setresidentwidgets(self):
        clockin = Button(self.residentTab, text="Clock In")
        clockin.grid(row=3, rowspan=1, columnspan=2, column=1)
        clockout = Button(self.residentTab, text="Clock Out")
        clockout.grid(row=3, column=3)





