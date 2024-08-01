from abc import ABC, abstractmethod


# ------------------------------------------------------------------#
#   This function is used to get the path of the file to read/write
#   the student details and payment details.
#   The function takes two parameters
#   1. StudentType: This parameter is used to get the type of student
#   2. dataORpayment: This parameter is used to get the type of data
def getPath(StudentType, dataORpayment):
    if StudentType == "PG" and dataORpayment == "data":
        return "data/pg_students.txt"
    elif StudentType == "PG" and dataORpayment == "payment":
        return "data/pg_payment.txt"
    elif StudentType == "UG" and dataORpayment == "data":
        return "data/ug_students.txt"
    elif StudentType == "UG" and dataORpayment == "payment":
        return "data/ug_payment.txt"
    else:
        return None


# ------------------------------------------------------------------#


class Student(ABC):
    initialId = 20220000

    @abstractmethod
    # -----------------------------------------------------------------------------------#
    def __init__(self, studentName, gender, year, classId, payment, studentType):
        self.studentId = Student.dynamicId()
        try:
            path = getPath(studentType, "payment")
            if path:
                if not self.isStudentExist(self.studentId, studentType):
                    with open(path, "a+") as file:
                        file.write(f"Student name: {studentName.capitalize() }, ")
                        file.write(f"Student ID : {self.studentId}, ")
                        file.write(f"{payment}\n")
                    path = getPath(studentType, "data")
                    with open(path, "a+") as file:
                        file.write(f"{self.studentId}, ")
                        file.write(f"{studentName}, ")
                        file.write(f"{gender.capitalize()}, ")
                        file.write(f"{year}, ")
                        file.write(f"{classId}\n")
                    print("-------------------------------------------------")
                    print("Student details have been written to the file.")
                    print("-------------------------------------------------")
                else:
                    print("-------------------------------------------------")
                    print("Student already exists")
                    print("-------------------------------------------------")
        except Exception as e:
            print(f"An error occurred: {e}")

    # -----------------------------------------------------------------------------------#
    # -------------------------------------------------------------#
    # StudentDetails() – This static method is used to get the student details from the file
    # The method takes one parameter with default value None used to get student type
    # If the student type is not provided then the method will get the details of both UG and PG students
    @staticmethod
    def StudentDetails(StudentType=None):
        try:
            if StudentType:
                path = getPath(StudentType, "data")
                if path:
                    with open(path, "r") as file:
                        data = file.read()
                        print(data)
            else:
                path = getPath("PG", "data")
                if path:
                    with open(path, "r") as file:
                        data = file.read()
                        print("PG Students Details: ")
                        print(data)
                path = getPath("UG", "data")
                if path:
                    with open(path, "r") as file:
                        data = file.read()
                        print("UG Students Details: ")
                        print(data)
        except Exception as e:
            print(f"An error occurred: {e}")

    # -------------------------------------------------------------#
    # payFees() – This method is used to get the payment details of the student
    # The method takes one parameter with default value None used to get student type
    # If the student type is not provided then the method will get the payment details of both UG and PG students
    # else it will print the payment details for the student type provided
    @staticmethod
    def payFees(studentType: str = None):
        try:
            if studentType:
                path = getPath(studentType, "payment")
                if path:
                    with open  (path, "r") as file:
                        status = file.read()
                        print(status)
            else:
                path = getPath("PG", "payment")
                if path:
                    with open(path, "r") as file:
                        status = file.read()
                        print(status)
                path = getPath("UG", "payment")
                if path:
                    with open(path, "r") as file:
                        status = file.read()
                        print(status)
        except Exception as e:
            print(f"An error occurred: {e}")

    # -------------------------------------------------------------#

    def isStudentExist(self, studentId, studentType):
        try:
            path = getPath(studentType, "data")
            if path:
                with open(path, "r") as file:
                    data = file.read()
                    if str(studentId) in data:
                        return True
                    else:
                        return False
        except Exception as e:
            print(f"An error occurred: {e}")

    @classmethod
    def dynamicId(self):
        self.initialId += 1
        return self.initialId

    @staticmethod
    def addStudent(studentName, gender, year, classId, payment):
        pass

    # -------------------------------------------------------------#
    # IsPresent() – This method shows whether the student is present to the college on a particular date.
    @staticmethod
    def IsPresent(date):
        day = date.strftime("%A")
        if day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]:
            return True
        else:
            return False
