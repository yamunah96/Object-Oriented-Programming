class Vehicle:
    #  common info
    def __init__(self,vehicle_no:str=None,brand_name:str=None, driver_name:str=None,distance:float=0):
        self.vehicle_no= vehicle_no
        self.brand_name= brand_name
        self.driver_name= driver_name
        self.distance= distance

    # calcualte total travel fare
    def calculate_fare(self):
        return self.distance*self.price_per_km

    def display(self):
        print("Your Cab has booked successfully.. Enjoy the ride")
        print(f"Driver:{self.driver_name}\nDistance:{self.distance}KM\nRate:₹{self.price_per_km}/KM\nTotal Fare: ₹{self.calculate_fare()}")

#  child class -- Car
class Car(Vehicle):
    price_per_km=10

#  child class -- Bike
class Bike(Vehicle):
    price_per_km=5
try:
    vehicle_type= input("Select the vehicle Car/Bike: ").lower().strip()

    if vehicle_type == "car":
        vehicle_no= input("Enter the vehicle no: ").lower().strip()
        driver= input("Enter the driver name: ").lower().strip()
        brand_name= input("Enter car brand name: ").lower().strip()
        distance= float(input("Enter travel distance in KM: "))
        vehicle= Car(vehicle_no,brand_name,driver,distance)
    elif vehicle_type == "bike":
        vehicle_no= input("Enter the vehicle no: ").lower().strip()
        driver= input("Enter the driver name: ").lower().strip()
        brand_name= input("Enter car brand name: ").lower().strip()
        distance= float(input("Enter travel distance in KM: "))
        vehicle= Bike(vehicle_no,brand_name,driver,distance)
    else:
        print("enter the valid vehicle_type")

    if vehicle:
        vehicle.display()
    else:
        print("Unable to book the ride")

except Exception as e:
    print(e)