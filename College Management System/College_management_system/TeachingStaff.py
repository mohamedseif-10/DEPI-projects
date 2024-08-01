from Staff import Staff

class TeachingStaff(Staff):
    def __init__(self, staffName, DepartmentId, salary, staffType="Teaching"):
        super().__init__(staffName, DepartmentId, salary, staffType)
