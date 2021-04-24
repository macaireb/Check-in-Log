import sqlite3
import datetime

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
                tmp += str(row[4])
                temp.append(tmp)
        return temp


    def clock_in(self, resident_index):
        residents = self.get_residents()
        current = datetime.datetime.now()
        conn = sqlite3.connect("storage.db")
        cur = conn.cursor()
        print(residents[resident_index])
        cur.execute("INSERT INTO timeclock VALUES (?,'in', ?, ?, ?, ?, ?, ?, ?)", (residents[resident_index][-1], current.year, current.month,
                    current.day, current.hour, current.minute, current.second, current.microsecond))
        conn.commit()
        conn.close()


#only difference is the string in the query, representing the direction (in/out)
    def clock_out(self, resident_index):
        residents = self.get_residents()
        current = datetime.datetime.now()
        conn = sqlite3.connect("storage.db")
        cur = conn.cursor()
        print(residents[resident_index])
        cur.execute("INSERT INTO timeclock VALUES (?,'out', ?, ?, ?, ?, ?, ?, ?)",
                    (residents[resident_index][-1], current.year, current.month,
                     current.day, current.hour, current.minute, current.second, current.microsecond))
        conn.commit()
        conn.close()

    def add_resident(self, fname, lname, floor=4):
        conn = sqlite3.connect("storage.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO residents VALUES (?, ?, ?, 'resident')", (fname, lname, floor))
        conn.commit()
        conn.close()


    ##get_residents returns a list, but for peace of mind, insure that when ROWID > 1 digit that the slicing still works
    ##to select all digits
    def delete_resident(self, resident_index):
        residents = self.get_residents()
        conn = sqlite3.connect("storage.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM residents WHERE ROWID=?", residents[resident_index][-1])
        conn.commit()
        conn.close()