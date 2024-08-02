import datetime
from allModules import *


def addUGStudent(studentName, gender, year, classId, payment):
    studentObject = UGStudent(studentName, gender, year, classId, payment)
    return studentObject


def addPGStudent(studentName, gender, year, classId, payment):
    studentObject = PGStudent(studentName, gender, year, classId, payment)
    return studentObject


def addTeachingStaff(staffName, DepartmentId, salary):
    return TeachingStaff(staffName, DepartmentId, salary, "Teaching")


def addNonTeachingStaff(staffName, DepartmentId, salary):
    return NonTeachingStaff(staffName, DepartmentId, salary, "Teaching")


def addGirlsHostel(studentId, blockNumber, roomNumber, hostelType="GirlsHostel"):
    obj = GirlsHostel(studentId, blockNumber, roomNumber, hostelType)
    return obj


def addBoysHostel(studentId, blockNumber, roomNumber, hostelType="BoysHostel"):
    obj = BoysHostel(studentId, blockNumber, roomNumber, hostelType)
    return obj


def addDepartment(departmentId, departmentName, hodName, totalStaffs, totalStudents):
    newObj = Department(
        departmentId, departmentName, hodName, totalStaffs, totalStudents
    )
    return newObj


def isStudentPresent(date):
    if Student.IsPresent(date):
        print("Student is present")
    else:
        print("This is holiday")


def deleteFiles():
    try:
        path = getPath("UG", "data")
        if path:
            with open(path, "w") as file:
                file.write("")
        path = getPath("PG", "data")
        if path:
            with open(path, "w") as file:
                file.write("")
        path = getPath("UG", "payment")
        if path:
            with open(path, "w") as file:
                file.write("")
        path = getPath("PG", "payment")
        if path:
            with open(path, "w") as file:
                file.write("")
        path = getPath("GirlsHostel", "data")
        if path:
            with open(path, "w") as file:
                file.write("")
        path = getPath("BoysHostel", "data")
        if path:
            with open(path, "w") as file:
                file.write("")
        path = getPath("Teaching", "data")
        if path:
            with open(path, "w") as file:
                file.write("")
        path = getPath("NonTeaching", "data")
        if path:
            with open(path, "w") as file:
                file.write("")
    except Exception as e:
        print(f"An error occurred: {e}")


class CollegeManagement:
    def __init__(self, CollegeName, City, ContactNumber):
        self.CollegeName = CollegeName
        self.City = City
        self.ContactNumber = ContactNumber

    def Open(self):
        today = datetime.datetime.now().weekday()
        if today in (4, 5):
            print(f"Today is {today} college is Closed")
        else:
            print(f"Today is {today} college is Open")

    def CollegeDetails(self):
        print("College Name: ", self.CollegeName)
        print("City: ", self.City)
        print("Contact Number: ", self.ContactNumber)

    # Implement the composition
    def addGirlsHostel(studentId, blockNumber, roomNumber, hostelType="GirlsHostel"):
        obj = GirlsHostel(studentId, blockNumber, roomNumber, hostelType)
        return obj

    def addBoysHostel(studentId, blockNumber, roomNumber, hostelType="BoysHostel"):
        obj = BoysHostel(studentId, blockNumber, roomNumber, hostelType)
        return obj

    def parking(vehicleNumber, vehicleOwnerName):
        parkObj = Parking(vehicleNumber, vehicleOwnerName)
        return parkObj

    def show_menu(self):

        while True:
            print("Welcome to College Management System!")
            print("1. Manage Students")
            print("2. Manage Hostels")
            print("3. Manage Departments")
            print("4. Manage Staff")
            print("5. Manage Parking")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                while True:
                    userInput = input(
                        "1: Add student.\n2: Show student details.\n3: Students payment details.\n4: Exit.\n"
                    )
                    if userInput == "1":
                        studentType = input("1: UG Student.\n2: PG Student.\n")
                        if studentType == "1":
                            addUGStudent(
                                input("Enter student name: "),
                                input("Enter student gender: "),
                                input("Enter student year: "),
                                input("Enter class id: "),
                                input("Enter payment paid or unpaid: "),
                            )
                        elif studentType == "2":
                            addPGStudent(
                                input("Enter student name: "),
                                input("Enter student gender:"),
                                input("Enter student year: "),
                                input("Enter class id: "),
                                input("Enter payment paid or unpaid: "),
                            )
                        else:
                            print("-------------------------------------------------")
                            print("Invalid choice!")
                            print("-------------------------------------------------")
                    elif userInput == "2":
                        Student.StudentDetails()
                    elif userInput == "3":
                        Student.payFees()
                    elif userInput == "4":
                        break
                    else:
                        print("-------------------------------------------------")
                        print("Invalid choice!")
                        print("-------------------------------------------------")
            elif choice == "2":
                while True:
                    userInput = input(
                        "1: Add hostel.\n2: Show hostel details.\n3: Exit.\n"
                    )
                    if userInput == "1":
                        hostelType = input("1: Girls Hostel.\n2: Boys Hostel.\n")
                        if hostelType == "1":
                            addGirlsHostel(
                                input("Enter student id: "),
                                input("Enter block number: "),
                                input("Enter room number: "),
                            )
                        elif hostelType == "2":
                            addBoysHostel(
                                input("Enter student id: "),
                                input("Enter block number: "),
                                input("Enter room number: "),
                            )
                        else:
                            print("-------------------------------------------------")
                            print("Invalid choice!")
                            print("-------------------------------------------------")

                    elif userInput == "2":
                        Hostel.HostelDetails()
                    elif userInput == "3":
                        break
                    else:
                        print("-------------------------------------------------")
                        print("Invalid choice!")
                        print("-------------------------------------------------")
            elif choice == "3":
                while True:
                    userInput = input(
                        "1: Add department.\n2: Department details.\n3: Show events.\n4: Exit.\n"
                    )
                    if userInput == "1":
                        addDepartment(
                            input("Enter department id: "),
                            input("Enter department name: "),
                            input("Enter HOD name: "),
                            input("Enter total staffs: "),
                            input("Enter total students: "),
                        )
                    elif userInput == "2":
                        Department.DepartmentDetails()
                    elif userInput == "3":
                        Department.showEvents()
                    elif userInput == "4":
                        break
                    else:
                        print("-------------------------------------------------")
                        print("Invalid choice!")
                        print("-------------------------------------------------")

            elif choice == "4":
                while True:
                    userInput = input(
                        "1: Add staff.\n2: Show staff details.\n3: Exit.\n"
                    )
                    if userInput == "1":
                        staffType = input(
                            "1: Teaching Staff.\n2: Non-Teaching Staff.\n"
                        )
                        if staffType == "1":
                            addTeachingStaff(
                                input("Enter staff name: "),
                                input("Enter department id: "),
                                input("Enter salary: "),
                            )
                        elif staffType == "2":
                            addNonTeachingStaff(
                                input("Enter staff name: "),
                                input("Enter department id: "),
                                input("Enter salary: "),
                            )
                        else:
                            print("-------------------------------------------------")
                            print("Invalid choice!")
                            print("-------------------------------------------------")
                    elif userInput == "2":
                        Staff.staffDetails()
                    elif userInput == "3":
                        break
                    else:
                        print("-------------------------------------------------")
                        print("Invalid choice!")
                        print("-------------------------------------------------")
            elif choice == "5":
                while True:
                    userInput = input("1: Park vehicle.\n2: Exit.\n")
                    if userInput == "1":
                        vehicleNumber = input("Enter vehicle number: ")
                        vehicleOwnerName = input("Enter vehicle owner name: ")
                        if self.parking(vehicleNumber, vehicleOwnerName):
                            print("Vehicle details have been written to the file.")
                        else:
                            print(
                                "Slot already reserved insert another slot to park the vehicle :"
                            )
                    elif userInput == "2":
                        break
                    else:
                        print("-------------------------------------------------")
                        print("Invalid choice!")
                        print("-------------------------------------------------")
            elif choice == "6":
                print("College Management System is closed!")
                break
            else:
                print("-------------------------------------------------")
                print("Invalid choice!")
                print("-------------------------------------------------")
