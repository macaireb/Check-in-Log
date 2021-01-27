from tkinter import *
from tkinter.ttk import *
from person import Person
from log import Log


class Menu(Notebook):
    residentTab = None
    names = ['macaire', 'leonard', 'james']
    namessix = ['shirley', 'colette', 'brayleigh']
    namesseven = ['warren', 'donna', 'vonnie']

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
        self.pack()

    def setlistbox(self, floor="Fourth Floor", c=1, r=3, cspan=1, rspan=1, namelist=names):
        curfloor = Label(self.residentTab, text=floor, style="BW.TLabel")
        curfloor.grid(row=2, rowspan=1, column=c, columnspan=1)
        namesvar = StringVar(value=namelist)
        namesbox = Listbox(self.residentTab, listvariable=namesvar, height=10) #add scrollable option later
        namesbox.grid(row=r, rowspan=rspan, column=c, columnspan=cspan)

    def setresidentwidgets(self):
        fourradio = Radiobutton(self.residentTab, text="Fourth Floor", style="BW.TRadiobutton", value=0, command=self.setlistbox())
        fourradio.grid(row=1, rowspan=1, column=2, columnspan=1)
        sixradio = Radiobutton(self.residentTab, text="Sixth Floor", style="BW.TRadiobutton", value=1)
        sixradio["command"]=self.setlistbox(floor="Sixth Floor", c=3, namelist=self.namessix)
        sixradio.grid(row=1, rowspan=1, column=4, columnspan=1)
        sevenradio = Radiobutton(self.residentTab, text="Seventh Floor", style="BW.TRadiobutton", value=2)
        sevenradio["command"]=self.setlistbox(floor="Seventh Floor", c=5, namelist=self.namesseven)
        sevenradio.grid(row=1, rowspan=1, column=6, columnspan=1)
        clockin = Button(self.residentTab, text="Clock In", style="BW.TButton")
        clockin.grid(row=4, rowspan=1, columnspan=1, column=1)
        clockout = Button(self.residentTab, text="Clock Out", style="BW.TButton")
        clockout.grid(row=4, column=3)

    def ClockIn(self): pass