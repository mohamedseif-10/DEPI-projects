from allModules import Student


class PGStudent(Student):
    def __init__(self, studentName, gender, year, classId, payment, studentType="PG"):
        super().__init__(studentName, gender, year, classId, payment, studentType)


