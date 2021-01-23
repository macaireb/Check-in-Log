class Log():
    auth, authNote = None,None  # What is this fragment?

    def __init__(self, date, time, inflag):
        self.date = date
        self.time = time
        self.inside = inflag
        self.log = []

    def entry(self, date, time, inside):
        if self.auth == None:
            self.log.append([date, time, inside])
        elif self.auth > 0:
            self.log.append([date, time, self.auth, self.authNote, inside])
        else:
            self.log.append(["entry bug"])

    def __add__(self, E):
        pass

    # if not isinstance(E,Log): return None
    # else:self.log + [E.date,E.time, E.inflag])

    def conflict(self):
        einflagstr = ''.join([str(i[2]) for i in self.log])  # Should look like 'FalseTrueFalseTrue…'
        DoubleIn = 'TrueTrue' in einflagstr  # upgrade one day to return [self.log[i][0] for i,val in enumerate(self.log[:-1]) if val[2]==self.log[i+1][2]]
        DoubleOut = 'FalseFalse' in einflagstr  # won't need after update
        return DoubleIn | DoubleOut
