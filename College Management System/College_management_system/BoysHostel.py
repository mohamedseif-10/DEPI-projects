from Hostel import Hostel


class BoysHostel(Hostel):
    def __init__(self, studentId, blockNumber, roomNumber, hostelType="BoysHostel"):
        super().__init__(studentId, blockNumber, roomNumber, hostelType)
