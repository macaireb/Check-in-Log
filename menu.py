from tkinter import *
from tkinter.ttk import *
from person import Person
from log import Log


class Menu(Notebook):
    residentTab = None
    names = ['macaire', 'leonard', 'james']
    namessix = ['shirley', 'colette', 'brayleigh']
    namesseven = ['warren', 'donna', 'vonnie']
    fourstr, sixstr, sevenstr = None, None, None
    namesbox = [Listbox(), Listbox(), Listbox()]

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.residentTab = Frame()
        self.add(self.residentTab, text="Residents")
        self.fourstr = StringVar(value=self.names)
        self.sixstr = StringVar(value=self.namessix)
        self.sevenstr = StringVar(value=self.namesseven)
        style = Style()
        style.configure("BW.TLabel", foreground="blue", background="white")
        style.configure("BW.TRadiobutton", foreground="blue", background="white")
        style.configure("BW.TButton", foreground="blue", background="white")
        ##Put Radio Boxes in __init__ and redraw based on selection, include tab.destroy
        self.pack()

    def setlistbox(self, floor="Fourth Floor", c=1, r=3, cspan=1, rspan=1, namelist=names):
        curfloor = Label(self.residentTab, text=floor, style="BW.TLabel")
        curfloor.grid(row=2, rowspan=1, column=c, columnspan=1)
        namesvar = StringVar(value=namelist)
        namesbox = Listbox(self.residentTab, listvariable=namesvar, height=10) #add scrollable option later
        namesbox.grid(row=r, rowspan=rspan, column=c, columnspan=cspan)

    def setresidentwidgets(self):
        fourradio = Radiobutton(self.residentTab, text="Fourth Floor", style="BW.TRadiobutton", value=0, command=self.fourfloorcolumns)
        fourradio.grid(row=1, rowspan=1, column=2, columnspan=1)
        sixradio = Radiobutton(self.residentTab, text="Sixth Floor", style="BW.TRadiobutton", value=1, command=self.sixfloorcolumns)
        sixradio.grid(row=1, rowspan=1, column=4, columnspan=1)
        sevenradio = Radiobutton(self.residentTab, text="Seventh Floor", style="BW.TRadiobutton", value=2, command=self.sevenfloorcolumns)
        sevenradio.grid(row=1, rowspan=1, column=6, columnspan=1)

    def fourfloorcolumns(self):
        self.namesbox[0] = Listbox(self.residentTab, listvariable=self.fourstr, height=10)
        self.namesbox[0].grid(column=1, row=3)
        self.namesbox[1] = Listbox(self.residentTab, listvariable=self.sixstr, height=10)
        self.namesbox[1].grid(column=3, row=3)
        self.namesbox[2] = Listbox(self.residentTab, listvariable=self.sevenstr, height=10)
        self.namesbox[2].grid(column=5, row=3)
        self.bindboxes()


    def sixfloorcolumns(self):
        self.namesbox[0] = Listbox(self.residentTab, listvariable=self.sixstr, height=10)
        self.namesbox[0].grid(column=1, row=3)
        self.namesbox[1] = Listbox(self.residentTab, listvariable=self.sevenstr, height=10)
        self.namesbox[1].grid(column=3, row=3)
        self.namesbox[2] = Listbox(self.residentTab, listvariable=self.fourstr, height=10)
        self.namesbox[2].grid(column=5, row=3)
        self.bindboxes()

    def sevenfloorcolumns(self):
        self.namesbox[0] = Listbox(self.residentTab, listvariable=self.sevenstr, height=10)
        self.namesbox[0].grid(column=1, row=3)
        self.namesbox[1] = Listbox(self.residentTab, listvariable=self.sixstr, height=10)
        self.namesbox[1].grid(column=3, row=3)
        self.namesbox[2] = Listbox(self.residentTab, listvariable=self.fourstr, height=10)
        self.namesbox[2].grid(column=5, row=3)
        self.bindboxes()

    def bindboxes(self):
        for i in self.namesbox:
            i.bind('<<ListboxSelect>>', self.showbuttons)

    def showbuttons(self, Event = None):
        for i in self.namesbox:
            ndex = i.curselection()
            if ndex != ():
                self.clockin = Button(self.residentTab, text="Clock In", style="BW.TButton")
                self.clockin.grid(row=4, rowspan=1, columnspan=1, column=1)
                self.clockout = Button(self.residentTab, text="Clock Out", style="BW.TButton")
                self.clockout.grid(row=4, column=3)


    def ClockIn(self): pass