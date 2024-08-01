class Parking:
    initialID = 0

    def dynamicId(self):
        self.initialID += 1
        return self.initialID

    def __init__(self, vehicleNumber, vehicleOwnerName):
        self.slotId = self.dynamicId()
        self.vehicleNumber = vehicleNumber
        self.vehicleOwnerName = vehicleOwnerName
        self.parkVehicle()

    def isReserved(self):
        try:
            with open("data/parking.txt", "r") as file:
                data = file.read()
                if str(self.slotId) in data:
                    return True
                else:
                    return False
        except Exception as e:
            print(f"An error occurred: {e}")

    def parkVehicle(self):
        try:
            if not self.isReserved():
                with open("data/parking.txt", "a+") as file:
                    file.write(f"Slot ID: {self.slotId}, ")
                    file.write(f"Vehicle Number: {self.vehicleNumber}, ")
                    file.write(f"Vehicle Owner Name: {self.vehicleOwnerName}\n")
                return True
            else:
                return False

        except Exception as e:
            print(f"An error occurred: {e}")


