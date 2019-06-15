import personclass as pc

class Student(pc.Person):
    def __init__(self):
        pc.Person.__init__(self)
        self.studentID = 0
        self.favBooks = []
        self.awards = []
        self.subjects = []
    def GetStudentID(self):
        return self.GetStudentID
    def GetAwards(self):
        return self.awards
     
