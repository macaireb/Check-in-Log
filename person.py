
class Person():
    def __init__(self, counselor, floor, lname, fname, mname=None, enrolled=True, released=False):
        self.counselor = counselor
        self.floor = floor
        self.lname = lname
        self.fname = fname
        self.mname = mname
        self.enrolled = enrolled
        self.released = released

    def __str__(self): return ' '.join([str(self.floor), self.fname, ['', self.mname][bool(self.mname)], self.lname])

    def __repr__(self): return 'Person(' + self.counselor + ', ' + str(self.floor) + ', ' + self.lname + ', ' + self.fname + \
                               ['', ', ' + self.mname][bool(self.mname)] + ')'

    def status(self): return self.log[-1][-1]

    def report(self): pass
    #Do duration check, direction conflict

    def release(self): self.released = True

