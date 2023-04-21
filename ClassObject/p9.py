class stu:
    def __init__(self):
        self.name = ""
        self.roll = 0
    def setstu(self):
        self.name = input("Enter student name = ")
        self.roll = int(input("Enter student Roll.No = "))
    def printstu(self):
        print("Student Name is ",self.name)
        print("Student Roll.No is ",self.roll)
class Exam(stu):
    def __init__(self):
        self.eng = 0
        self.math = 0
        self.sci = 0
    def setex(self):
        self.eng = int(input("Enter the marks of English = "))
        self.math = int(input("Enter the marks of Maths = "))
        self.sci = int (input("Enter the marks of Science = "))
    def printex(self):
        print("English = ",self.eng,"Maths = ",self.math,"Science = ",self.sci)
class Result(Exam):
    def __init__(self):
        self.t = 0
    def setres(self):
        self.t = self.sci + self.math + self.eng
    def printres(self):
        print("Result = ",self.t)

R1=Result()
R1.setstu()
R1.setex()
R1.setres()
R1.printstu()
R1.printex()
R1.printres()