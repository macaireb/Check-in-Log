import sqlite3

class DB_interface():
    def get_residents(self, floor=4):
        con = sqlite3.connect('storage.db')
        cur = con.cursor()
        if floor == 4:
            cur.execute("SELECT *, ROWID FROM residents WHERE floor=4")
        self.fourth_floor = cur.fetchall()
            #need to convert this list of tuples into a list of strings
        con.close()
        tmp = str()
        temp = list()
        if type(self.fourth_floor == list):
            for row in self.fourth_floor:
                tmp = str()
                for i in range(2):
                    tmp += str(row[i]) + ' '
                temp.append(tmp)
        return temp

    def check_resi_clock(self, residents):
        conn = sqlite3.connect("storage.db")
        cur = conn.cursor()
        #Format for resident clock table will be fname_lname_clock
        t_name = (residents[0] + "_" + residents[1] + "_clock", )
        tmp = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", t_name)
        #If resident has no clock table in SQLite, create one
        if tmp.fetchone() == None:
            cur.execute('''CREATE TABLE ? (direction text, time integer)''')
            conn.commit()
        conn.close()

    def punch_resi_clock(self, resident, direction):
        conn = sqlite3.connect("storage.db")
        cur = conn.cursor()


        conn.close()