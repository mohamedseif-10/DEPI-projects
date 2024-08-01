from Staff import Staff


class NonTeachingStaff(Staff):
    def __init__(self, staffName, DepartmentId, salary, staffType="NonTeaching"):
        super().__init__(staffName, DepartmentId, salary, staffType)


# addNonTeachingStaff("Ali", 100, 40000)
# addNonTeachingStaff("Mohamed", 101, 50000)
# addNonTeachingStaff("Ahmed", 102, 60000)

# Staff.staffDetails("Teaching")
# Staff.staffDetails("NonTeaching")
# Staff.staffDetails()
