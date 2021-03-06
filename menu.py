import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
import DB_interface


###
# Need to change class to frame, and create a window manager class(notebook) to hold and manage those frames
###

class MainMenu(Frame):
    resident_view_btn, counselor_edit_btn, resident_view, counselor_edit = None, None, None, None
    check_punch, check_punches_btn = None, None

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.DB = DB_interface.DB_interface()
        style = Style()
        style.configure("BW.TLabel", foreground="blue", background="white")
        style.configure("BW.TRadiobutton", foreground="blue", background="white")
        style.configure("BW.TButton", foreground="blue", background="white")
        # Put Radio Boxes in __init__ and redraw based on selection, include tab.destroy
        self.main_menu = Button(self, text="Menu", command=self.draw_main_menu, style="BW.TButton")
        self.main_menu.grid(row=1, rowspan=1, column=1, columnspan=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.pack()
        self.draw_main_menu()

    def draw_main_menu(self):
        print("Called draw main menu")
        try:
            print("Inside try of drawing main menu")
            if self.counselor_edit.winfo_exists() == 1:
                self.counselor_edit.destroy_counselor_resident_menu()
                self.counselor_edit.destroy()
        except AttributeError:
            print("Attribute error occurred")
        try:
            if self.resident_view.winfo_exists() == 1:
                self.resident_view.destroy_resident_punch()
                self.resident_view.destroy()
        except AttributeError:
            print("resident view doesnt exist")
        try:
            if self.check_punch.winfo_exists() == 1:
                print("It thinks the check punch view exists")
                self.check_punch.destroy_view_punches()
                self.check_punch.destroy()
        except AttributeError:
            print("View punches doesn't exist")
        self.resident_view_btn = Button(self, text="Resident Check In", style="BW.TButton",
                                        command=self.show_resident_punch)
        self.resident_view_btn.grid(row=1, rowspan=1, column=2, columnspan=2)
        self.counselor_edit_btn = Button(self, text="Edit Residents", style="BW.TButton",
                                         command=self.show_counselor_edit)
        self.counselor_edit_btn.grid(row=2, rowspan=1, column=2, columnspan=2)
        self.check_punches_btn = Button(self, text="Check Punches", style="BW.TButton",
                                        command=self.show_check_punches)
        self.check_punches_btn.grid(row=3, column=2)

    def show_counselor_edit(self):
        self.destroy_main_menu()
        self.counselor_edit = CounselorsResidentMenu()

    def show_resident_punch(self):
        self.destroy_main_menu()
        self.resident_view = ResidentPunchMenu()

    def show_check_punches(self):
        self.destroy_main_menu()
        self.check_punch = ViewPunches()

    def destroy_main_menu(self):
        if self.resident_view_btn.winfo_exists() == 1:
            self.resident_view_btn.destroy()
        if self.counselor_edit_btn.winfo_exists() == 1:
            self.counselor_edit_btn.destroy()
        if self.check_punches_btn.winfo_exists() == 1:
            self.check_punches_btn.destroy()


class ResidentPunchMenu(Frame):
    resident_list, resident_strs, clock_in, clock_out = None, None, None, None

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.DB = DB_interface.DB_interface()
        style = Style()
        style.configure("BW.TLabel", foreground="blue", background="white")
        style.configure("BW.TRadiobutton", foreground="blue", background="white")
        style.configure("BW.TButton", foreground="blue", background="white")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.draw()

    def draw(self):
        self.resident_strs = StringVar(value=self.DB.get_residents())
        self.resident_list = Listbox(self, listvariable=self.resident_strs, height=15)
        self.resident_list.grid(row=2, column=1, columnspan=2)
        self.clock_in = Button(self, text="Clock In", style="BW.TButton", command=self.punch_clock_in)
        self.clock_in.grid(row=4, rowspan=1, columnspan=1, column=2)
        self.clock_out = Button(self, text="Clock Out", style="BW.TButton", command=self.punch_clock_out)
        self.clock_out.grid(row=4, column=3)
        self.pack()

    def punch_clock_in(self):
        ###
        # Will have to use radio buttons, once again, to toggle through the different floors.
        # clock in and out functions will have to determine which radiobox is active, to select
        # correct resident
        ###
        if self.resident_list.curselection() != ():
            print(str(self.resident_list.curselection()[0]))
            self.DB.clock_in(self.resident_list.curselection()[0])
            resident = self.DB.get_residents()
            resident = resident[self.resident_list.curselection()[0]][0:-2]
            clock_msg = tkinter.messagebox.Message(self, title="Success",
                                                   message="Clock in made for " + resident)
            clock_msg.show()

    def punch_clock_out(self):
        ###
        # Have to use two almost identical functions, because (I don't believe), one parameter can be nested in another.
        # As is the case for command= parameter
        ###
        if self.resident_list.curselection() != ():
            print(str(self.resident_list.curselection()[0]))
            self.DB.clock_out(self.resident_list.curselection()[0])
            resident = self.DB.get_residents()
            resident = resident[self.resident_list.curselection()[0]][0:-2]
            print(resident)
            clock_msg = tkinter.messagebox.Message(self, title="Success",
                                                   message="Clock out made for " + resident)
            clock_msg.show()

    def destroy_resident_punch(self):
        self.pack_forget()
        if self.resident_list.winfo_exists() == 1:
            self.resident_list.destroy()
        if self.clock_in.winfo_exists() == 1:
            self.clock_in.destroy()
        if self.clock_out.winfo_exists() == 1:
            self.clock_out.destroy()


class CounselorsResidentMenu(Frame):
    resident_list = None
    resident_strs = None

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.DB = DB_interface.DB_interface()
        style = Style()
        style.configure("BW.TLabel", foreground="blue", background="white")
        style.configure("BW.TRadiobutton", foreground="blue", background="white")
        style.configure("BW.TButton", foreground="blue", background="white")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.draw()

    def draw(self):
        self.resident_strs = StringVar(value=self.DB.get_residents())
        self.resident_list = Listbox(self, listvariable=self.resident_strs, height=15)
        self.resident_list.grid(column=1, columnspan=2, row=2)
        self.resi_fname = Label(self, style="BW.TLabel", text="First Name")
        self.resi_fname.grid(row=3, rowspan=1, column=1, columnspan=1)
        self.resi_lname = Label(self, style="BW.TLabel", text="Last Name")
        self.resi_lname.grid(row=3, rowspan=1, column=2, columnspan=1)
        self.add_resident = Button(self, style="BW.TButton",
                                   text="Add new resident", command=self.add_resi_to_db)
        self.add_resident.grid(row=4, rowspan=1, column=3, columnspan=1)
        self.fname_string = StringVar()
        self.add_resi_fname = Entry(self, textvariable=self.fname_string)
        self.add_resi_fname.grid(row=4, rowspan=1, column=1, columnspan=1)
        self.lname_string = StringVar()
        self.add_resi_lname = Entry(self, textvariable=self.lname_string)
        self.add_resi_lname.grid(row=4, rowspan=1, column=2, columnspan=1)
        self.delete_resident = Button(self, style="BW.TButton",
                                      text="Remove Resident", command=self.del_resi_from_db)
        self.delete_resident.grid(row=3, rowspan=1, column=3, columnspan=1)
        self.pack()

    def add_resi_to_db(self):
        valid = [False, False]
        ###
        # Need to add validation for names with a hyphen or comma, since they can be valid characters
        ###
        if self.fname_string.get().isalpha():
            valid[0] = True
        else:
            fname_msg = tkinter.messagebox.Message(self, title="Invalid",
                                                   message="Only letters are allowed, please correct First name")
            fname_msg.show()
        if self.lname_string.get().isalpha():
            valid[1] = True
        else:
            lname_msg = tkinter.messagebox.Message(self, title="Success",
                                                   message="Only letters are allowed, please correct Last name")
            lname_msg.show()
        if valid[0] & valid[1]:
            self.DB.add_resident(self.fname_string.get(), self.lname_string.get())
        self.redraw_list()

    def del_resi_from_db(self):
        resident = self.DB.get_residents()
        resident = resident[self.resident_list.curselection()[0]]
        if self.resident_list.curselection() != ():
            self.DB.delete_resident(self.resident_list.curselection()[0])
            complete = tkinter.messagebox.Message(self, title="Resident deleted",
                                                  message="Successfully deleted " + resident + "from database")
            complete.show()
            self.redraw_list()

    def redraw_list(self):
        if self.resident_list.winfo_exists() == 1:
            self.resident_list.destroy()
            print("deleting old listbox, to refresh")
        self.resident_strs = StringVar(value=self.DB.get_residents())
        self.resident_list = Listbox(self, listvariable=self.resident_strs, height=15)
        self.resident_list.grid(row=2, column=1, columnspan=2)

    def destroy_counselor_resident_menu(self):
        self.pack_forget()
        if self.resident_list.winfo_exists() == 1:
            self.resident_list.destroy()
        if self.add_resident.winfo_exists() == 1:
            self.add_resident.destroy()
        if self.delete_resident.winfo_exists() == 1:
            self.delete_resident.destroy()
        if self.add_resi_fname.winfo_exists() == 1:
            self.add_resi_fname.destroy()
        if self.add_resi_lname.winfo_exists() == 1:
            self.add_resi_lname.destroy()
        if self.resi_fname.winfo_exists() == 1:
            self.resi_fname.destroy()
        if self.resi_lname.winfo_exists() == 1:
            self.resi_lname.destroy()


class ViewPunches(Frame):
    resident_list, resident_strs, view_punches = None, None, None

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.DB = DB_interface.DB_interface()
        style = Style()
        style.configure("BW.TLabel", foreground="blue", background="white")
        style.configure("BW.TRadiobutton", foreground="blue", background="white")
        style.configure("BW.TButton", foreground="blue", background="white")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.draw()

    def draw(self):
        self.resident_strs = StringVar(value=self.DB.get_residents())
        self.residents_lbl = Label(self, text="Resident's List")
        self.residents_lbl.grid(row=2, column=1, columnspan=2)
        self.resident_list = Listbox(self, listvariable=self.resident_strs, height=15)
        self.resident_list.grid(row=3, column=1, columnspan=2)
        self.view_punches = Button(self, text="Check Resident's Times", style="BW.TButton", command=self.get_punches)
        self.view_punches.grid(row=4, column=1, columnspan=2)
        self.punches_list = Listbox(self, height=15)
        self.punches_list.grid(row=3, column=3, columnspan=2)
        self.pack()

    def destroy_view_punches(self):
        print("Entered destroy of view punches")
        if self.resident_list.winfo_exists() == 1:
            self.resident_list.destroy()
            print("Supposed to destroy resident list")
        if self.view_punches.winfo_exists() == 1:
            self.view_punches.destroy()
        if self.residents_lbl.winfo_exists() == 1:
            self.residents_lbl.destroy()
        if self.punches_list.winfo_exists() == 1:
            self.punches_list.destroy()
        self.pack_forget()

    def get_punches(self):
        try:
            if self.resident_list.curselection() != ():
                self.current_punches = self.DB.get_resi_punches(self.resident_list.curselection()[0])
                self.current_punches = StringVar(value=self.current_punches)
                if self.punches_list.winfo_exists() == 1:
                    self.punches_list.destroy()
                self.punches_list = Listbox(self, listvariable=self.current_punches, height=15)
                self.punches_list.grid(row=3, column=3, columnspan=2)
        except AttributeError:
            print("resident list has no value selected, so punches list can't propagate. Or no punches for resident")
