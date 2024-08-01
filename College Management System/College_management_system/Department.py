class Department:
    def __init__(self, departmentId, departmentName, hodName, totalStaffs, totalStudents):
        self.departmentId = departmentId
        self.departmentName = departmentName
        self.hodName = hodName
        self.totalStaffs = totalStaffs
        self.totalStudents = totalStudents

    def DepartmentDetails(self):
        print("Department Name:", self.departmentName)
        print("HOD Name:", self.hodName)
        print("Total Students:", self.totalStudents)

    def ShowEvents(self):
        file = open("data/events.txt", "r")
        data = file.read().split("\n")
        print("The available events : \n")
        for line in data:
            event = line.split(",")
            if event[0] == self.departmentName:
                print("Event Name:", event[1])
                print("Date:", event[2])
                print("Class Room:", event[3])
                print("Description:", event[4])
                print("----------------------------------------------------------")
        file.close()
