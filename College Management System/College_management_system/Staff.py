from abc import ABC, abstractmethod

def getPath(staffType):
    if staffType == "Teaching":
        return "data/TeachingStaff.txt"
    elif staffType == "NonTeaching":
        return "data/NonTeachingStaff.txt"
    else:
        return None

class Staff(ABC):
    initialId = 0
    @abstractmethod
    def __init__(self,  staffName, DepartmentId, salary, staffType = None):
        path = getPath(staffType)
        self.staffId = Staff.dynamicId()
        try:
            if path and not self.isStaffMemberExist(self.staffId, staffType):
                file = open(path, "a+")
                file.write(f"{self.staffId}, ")
                file.write(f"{staffName}, ")
                file.write(f"{DepartmentId}, ")
                file.write(f"{salary}\n")
                file.close()
                print("Staff details have been written to the file.")
            else:
                print("Staff already exists")
        except Exception as e:
            print(f"An error occurred: {e}")
    @staticmethod
    def staffDetails(staffType = None):
        path = getPath(staffType)
        if staffType:
            file = open(path, "r")
            data = file.read()
            print(data)
            file.close()
        else:
            path = getPath("Teaching")
            file = open(path, "r")
            data = file.read()
            print(data)
            file.close()
            path = getPath("NonTeaching")
            file = open(path, "r")
            data = file.read()
            print(data)
    def isStaffMemberExist(self, staffId, staffType):
        try:
            path = getPath(staffType)
            if path:
                with open(path, "r") as file:
                    data = file.read()
                    if str(staffId) in data:
                        return True
                    else:
                        return False
        except Exception as e:
            print(f"An error occurred: {e}")
    @classmethod
    def dynamicId(self):
        self.initialId += 1
        return self.initialId


# staff – There are two types of staff in the college. so this class is the base class of two child classes – TeachingStaff and NonTeachingStaff
# TeachingStaff – This class is the child class of staff. since TeachingStaff is a staff.
# NonTeachingStaff – This class is the child class of staff. since NonTeachingStaff is a staff.

# 4. staff :

# staffDetails() – This method contains the details of both teaching as well as non-teaching staff along with their salary details.
