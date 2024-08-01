from abc import ABC, abstractmethod


def getHostelPath(hostelType):
    if hostelType == "BoysHostel":
        return "data/BoysHostel.txt"
    elif hostelType == "GirlsHostel":
        return "data/GirlsHostel.txt"
    else:
        return None


class Hostel(ABC):

    @abstractmethod
    def __init__(self, studentId, blockNumber, roomNumber, hostelType=None):
        self.studentId = studentId
        try:
            path = getHostelPath(hostelType)
            if path:
                if not self.isReserved(studentId, roomNumber, hostelType):
                    with open(path, "a+") as file:
                        file.write(f"{studentId}, ")
                        file.write(f"{blockNumber}, ")
                        file.write(f"{roomNumber}\n")
                    print("Student details have been written to the file.")
                else:
                    print("Student reserved another room or room is already reserved.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def HostelDetails(hostelType=None):
        hostel_path = getHostelPath(hostelType)
        if hostel_path:
            with open(hostel_path, "r") as file:
                hostel_details = file.read()
            print("Hostel Details:")
            print(hostel_details)
        else:
            path = getHostelPath("BoysHostel")
            with open(path, "r") as file:
                data = file.read()
                print(data)
            path = getHostelPath("GirlsHostel")
            with open(path, "r") as file:
                data = file.read()
                print(data)

    def CheckIn(self):
        try:
            hostelType = (
                "BoysHostel"
                if self.__class__.__name__ == "BoysHostel"
                else "GirlsHostel"
            )
            path = getHostelPath(hostelType)
            with open(path, "r") as file:
                data = file.readlines()
                for line in data:
                    studentData = line.strip().split(", ")
                    if studentData[0] == self.studentId:
                        print("Yes, student checked in.")
                        return
            print("No, student not checked in.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def CheckOut(self):
        try:
            hostelType = (
                "BoysHostel"
                if self.__class__.__name__ == "BoysHostel"
                else "GirlsHostel"
            )
            path = getHostelPath(hostelType)
            with open(path, "r") as file:
                data = file.readlines()
                for line in data:
                    studentData = line.strip().split(", ")
                    if studentData[0] == self.studentId:
                        print("Student not checked out yet.")
                        return
                print("Yes, student checked out.")

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def isReserved(self, studentId, roomNumber, hostelType):
        try:
            path = getHostelPath(hostelType)
            if path:
                with open(path, "r") as file:
                    data = file.readlines()
                    for line in data:
                        studentData = line.strip().split(", ")
                        if studentData[0] == str(studentId) or studentData[2] == str(
                            roomNumber
                        ):
                            return True
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
