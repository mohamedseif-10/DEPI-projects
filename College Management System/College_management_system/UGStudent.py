from allModules import Student
class UGStudent(Student):
    def __init__(self, studentName, gender, year, classId, payment, studentType = "UG"):
        super().__init__(studentName, gender, year, classId, payment, studentType)