import tkinter.messagebox
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
        self.clockin = Button(self.residentTab, text="Clock In", style="BW.TButton", command=self.punch_clock_in)
        self.clockin.grid(row=4, rowspan=1, columnspan=1, column=2)
        self.clockout = Button(self.residentTab, text="Clock Out", style="BW.TButton", command=self.punch_clock_out)
        self.clockout.grid(row=4, column=3)

    def punch_clock_in(self):
        ###
        #Will have to use radio buttons, once again, to toggle through the different floors.
        #clock in and out functions will have to determine which radiobox is active, to select
        #correct resident
        ###
        if(self.namesbox[0].curselection() != ()):
            print(str(self.namesbox[0].curselection()[0]))
            self.DB.clock_in(self.namesbox[0].curselection()[0])
            resident = self.DB.get_residents()
            resident = resident[self.namesbox[0].curselection()[0]][0:-2]
            clock_msg = tkinter.messagebox.Message(self.residentTab, title="Success",
                                                      message= "Clock in made for " + resident)
            clock_msg.show()


    def punch_clock_out(self):
        ###
        #Have to use two almost identical functions, because (I don't believe), one parameter can be nested in another. As is the case for command= parameter
        ###
        if(self.namesbox[0].curselection() != ()):
            print(str(self.namesbox[0].curselection()[0]))
            self.DB.clock_out(self.namesbox[0].curselection()[0])
            resident = self.DB.get_residents()
            resident = resident[self.namesbox[0].curselection()[0]][0:-2]
            print(resident)
            clock_msg = tkinter.messagebox.Message(self.residentTab, title="Success",
                                                      message="Clock out made for " + resident)
            clock_msg.show()


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
        self.add_resident = Button(self.residentTab, style="BW.TButton",
                                   text="Add new resident", command=self.add_resi_to_db)
        self.add_resident.grid(row=4, rowspan=1, column=3, columnspan=1)
        self.fname_string = StringVar()
        self.add_resi_fname = Entry(self.residentTab, textvariable=self.fname_string)
        self.add_resi_fname.grid(row=4, rowspan=1, column=1, columnspan=1)
        self.lname_string = StringVar()
        self.add_resi_lname = Entry(self.residentTab, textvariable=self.lname_string)
        self.add_resi_lname.grid(row=4, rowspan=1, column=2, columnspan=1)
        self.delete_resident = Button(self.residentTab, style="BW.TButton",
                                      text="Remove Resident", command=self.del_resi_from_db)
        self.delete_resident.grid(row=3, rowspan=1, column=3, columnspan=1)

    def add_resi_to_db(self):
        valid = [False, False]
        ###
        #Need to add validation for names with a hyphen or comma, since they can be valid characters
        ###
        if self.fname_string.get().isalpha():
            valid[0] = True
        else:
            fname_msg = tkinter.messagebox.Message(self.residentTab, title="Invalid",
                                                   message="Only letters are allowed, please correct First name")
            fname_msg.show()
        if self.lname_string.get().isalpha():
            valid[1] = True
        else:
            lname_msg = tkinter.messagebox.Message(self.residentTab, title="Success",
                                                   message="Only letters are allowed, please correct Last name")
            lname_msg.show()
        if valid[0] & valid[1]:
            self.DB.add_resident(self.fname_string.get(), self.lname_string.get())
        for i in range(len(self.namesbox)):
            if self.namesbox[i].winfo_exists() == 1:
                self.namesbox[i].destroy()
            self.set_listboxes()
            self.fourfloorcolumns()

    def del_resi_from_db(self):
        resident = self.DB.get_residents()
        resident = resident[self.namesbox[0].curselection()[0]]
        if self.namesbox[0].curselection() != ():
            self.DB.delete_resident(self.namesbox[0].curselection()[0])
            complete = tkinter.messagebox.Message(self.residentTab, title="Resident deleted",
                                          message="Successfully deleted " + resident + "from database")
            complete.show()
            for i in range(len(self.namesbox)):
                if self.namesbox[i].winfo_exists() == 1:
                    self.namesbox[i].destroy()
                self.set_listboxes()
                self.fourfloorcolumns()

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
