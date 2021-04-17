from tkinter import *
from tkinter.ttk import *
import sqlite3
from person import Person
from log import Log
###
#Need to change class to frame, and create a window manager class(notebook) to hold and manage those frames
###

class menu(Notebook):
    residentTab = None
    namesfour = list()
    fourstr = None
    namesbox = [Listbox(), Listbox(), Listbox()]

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.residentTab = Frame()
        self.add(self.residentTab, text="Residents")
        style = Style()
        style.configure("BW.TLabel", foreground="blue", background="white")
        style.configure("BW.TRadiobutton", foreground="blue", background="white")
        style.configure("BW.TButton", foreground="blue", background="white")
        ##Put Radio Boxes in __init__ and redraw based on selection, include tab.destroy
        self.main_menu = Button(self.residentTab, text="Menu", command=self.draw_main_menu, style="BW.TButton")
        self.main_menu.grid(row=1, rowspan=1, column=1, columnspan=1)
        self.pack()

    def setresidentwidgets(self):
        self.getResidents()
        self.fourfloorcolumns()
        self.showbuttons()

    def getResidents(self, floor=4):
        con = sqlite3.connect('storage.db')
        cur = con.cursor()
        if floor == 4:
            cur.execute("SELECT *, ROWID FROM residents WHERE floor=4")
        self.namesfour = cur.fetchall()
            #need to convert this list of tuples into a list of strings
        con.close()
        tmp = str()
        temp = list()
        if type(self.namesfour == list):
            for row in self.namesfour:
                tmp = str()
                for i in range(2):
                    tmp += str(row[i]) + ' '
                temp.append(tmp)
        self.fourstr = StringVar(value=temp)

    def destroy_check_in(self):
        for i in range(len(self.namesbox)):
            if self.namesbox[i].winfo_exists() == 1:
                self.namesbox[i].destroy()
        try:
            if self.clockin.winfo_exists() == 1:
                self.clockin.destroy()
            if self.clockout.winfo_exists() == 1:
                self.clockout.destroy()
        except AttributeError: pass

    def fourfloorcolumns(self):
        self.namesbox[0] = Listbox(self.residentTab, listvariable=self.fourstr, height=10)
        self.namesbox[0].grid(column=1, row=3)
        self.namesbox[1] = Listbox(self.residentTab, listvariable=self.fourstr, height=10)
        self.namesbox[1].grid(column=2, row=3)
        self.namesbox[2] = Listbox(self.residentTab, listvariable=self.fourstr, height=10)
        self.namesbox[2].grid(column=3, row=3)

    def showbuttons(self, Event = None):
        self.clockin = Button(self.residentTab, text="Clock In", style="BW.TButton")
        self.clockin.grid(row=4, rowspan=1, columnspan=1, column=2)
        self.clockout = Button(self.residentTab, text="Clock Out", style="BW.TButton")
        self.clockout.grid(row=4, column=3)

    def draw_main_menu(self):
        self.destroy_check_in()
        self.check_in = Button(self.residentTab, text="Resident Check In", style="BW.TButton", command=self.setresidentwidgets)
        self.check_in.grid(row=1, rowspan=1, column=2, columnspan=2)

    def destroy_main_menu(self):
        if self.check_in.winfo_exists() == 1:
            self.check_in.destroy()

class CounselorsResidentMenu(Notebook):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.couns_tab = Frame()
        self.add(self.couns_tab, Text="Counselors")
