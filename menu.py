from tkinter import *
from tkinter.ttk import *
import DB_interface
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
        self.DB = DB_interface.DB_interface()
        style = Style()
        style.configure("BW.TLabel", foreground="blue", background="white")
        style.configure("BW.TRadiobutton", foreground="blue", background="white")
        style.configure("BW.TButton", foreground="blue", background="white")
        ##Put Radio Boxes in __init__ and redraw based on selection, include tab.destroy
        self.main_menu = Button(self.residentTab, text="Menu", command=self.draw_main_menu, style="BW.TButton")
        self.main_menu.grid(row=1, rowspan=1, column=1, columnspan=1)
        self.residentTab.columnconfigure(0, weight=1)
        self.residentTab.columnconfigure(1, weight=1)
        self.residentTab.columnconfigure(2, weight=1)
        self.residentTab.columnconfigure(3, weight=1)
        self.residentTab.columnconfigure(4, weight=1)
        self.pack()

    def setresidentwidgets(self):
        try:
            if self.resident_view.winfo_exists() == 1:
                self.resident_view.destroy()
            if self.resident_edit.winfo_exists() == 1:
                self.resident_edit.destroy()
        except AttributeError: pass
        self.set_listboxes()
        self.fourfloorcolumns()
        self.showbuttons()

    def set_listboxes(self):
        self.fourstr = StringVar(value=self.DB.get_residents())

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
        self.namesbox[0].grid(column=1, row=2)
        self.namesbox[1] = Listbox(self.residentTab, listvariable=self.fourstr, height=10)
        self.namesbox[1].grid(column=2, row=2)
        self.namesbox[2] = Listbox(self.residentTab, listvariable=self.fourstr, height=10)
        self.namesbox[2].grid(column=3, row=2)

    def showbuttons(self, Event = None):
        self.clockin = Button(self.residentTab, text="Clock In", style="BW.TButton")
        self.clockin.grid(row=4, rowspan=1, columnspan=1, column=2)
        self.clockout = Button(self.residentTab, text="Clock Out", style="BW.TButton")
        self.clockout.grid(row=4, column=3)

    def draw_main_menu(self):
        self.destroy_check_in()
        self.destroy_resident_edit()
        self.resident_view = Button(self.residentTab, text="Resident Check In", style="BW.TButton", command=self.setresidentwidgets)
        self.resident_view.grid(row=1, rowspan=1, column=2, columnspan=2)
        self.resident_edit = Button(self.residentTab, text="Edit Residents", style="BW.TButton", command=self.draw_resident_edit)
        self.resident_edit.grid(row=2, rowspan=1, column=2, columnspan=2)

    def destroy_main_menu(self):
        if self.resident_view.winfo_exists() == 1:
            self.resident_view.destroy()

    def draw_resident_edit(self):
        try:
            if self.resident_view.winfo_exists() == 1:
                self.resident_view.destroy()
            if self.resident_edit.winfo_exists() == 1:
                self.resident_edit.destroy()
        except AttributeError: pass
        self.set_listboxes()
        self.fourfloorcolumns()
        self.resi_fname = Label(self.residentTab, style="BW.TLabel", text="First Name")
        self.resi_fname.grid(row=3, rowspan=1, column=1, columnspan=1)
        self.resi_lname = Label(self.residentTab, style="BW.TLabel", text="Last Name")
        self.resi_lname.grid(row=3, rowspan=1, column=2, columnspan=1)
        self.add_resident = Button(self.residentTab, style="BW.TButton", text="Add new resident")
        self.add_resident.grid(row=4, rowspan=1, column=3, columnspan=1)
        self.add_resi_fname = Entry(self.residentTab)
        self.add_resi_fname.grid(row=4, rowspan=1, column=1, columnspan=1)
        self.add_resi_lname = Entry(self.residentTab)
        self.add_resi_lname.grid(row=4, rowspan=1, column=2, columnspan=1)
        self.delete_resident = Button(self.residentTab, style="BW.TButton", text="Remove Resident")
        self.delete_resident.grid(row=3, rowspan=1, column=3, columnspan=1)

    def destroy_resident_edit(self):
        for i in range(len(self.namesbox)):
            if self.namesbox[i].winfo_exists() == 1:
                self.namesbox[i].destroy()
        try:
            if self.resi_fname.winfo_exists() == 1:
                self.resi_fname.destroy()
            if self.resi_lname.winfo_exists() == 1:
                self.resi_lname.destroy()
            if self.add_resident.winfo_exists() == 1:
                self.add_resident.destroy()
            if self.add_resi_fname.winfo_exists() == 1:
                self.add_resi_fname.destroy()
            if self.add_resi_lname.winfo_exists() == 1:
                self.add_resi_lname.destroy()
            if self.delete_resident.winfo_exists() == 1:
                self.delete_resident.destroy()
        except AttributeError: pass


class CounselorsResidentMenu(Notebook):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.couns_tab = Frame()
        self.add(self.couns_tab, Text="Counselors")
