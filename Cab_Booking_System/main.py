# parent class
class Vehicle:
    def __init__(self,driver_name:str=None,vehicle_no:str=None,brand_name:str=None,price_per_km:float=0):
        # instance(object) attributes
        self.driver_name=driver_name
        self.vehicle_no=vehicle_no
        self.brand_name=brand_name
        self.price_per_km=price_per_km

    def display(self):
        return f"Driver: {self.driver_name}\nVehicle:{self.brand_name}\nVehicle_no:{self.vehicle_no}\nPrice Per KM: ₹{self.price_per_km}/KM"

# Child class car
class Car(Vehicle):
    pass

# Child class bike
class Bike(Vehicle):
    pass

car1=Car("Rahul","KA1234","Toyota",8)
car2= Car("Yash","KA2626","Maruti Suzki",6)

bike1=Bike("Rina","KA7680","Tvs",5)
bike2= Bike("Gagan","KA9090","Active Honda",6)

vehicle_avilable={
    "car":[car1,car2],
    "bike":[bike1,bike2]
}
while True:
    vehicle_type= input("enter vehicle type Car/Bike: ").lower().strip()
    if vehicle_type in vehicle_avilable:
        print("="*70)
        for data in vehicle_avilable[vehicle_type]:
            print(data.display())
            print("="*70)
        vehicle_no= input("enter vehicle_no to book a ride: ").lower().strip()
        selected_vehicle=None

        for data in vehicle_avilable[vehicle_type]:
            if vehicle_no == data.vehicle_no.lower():
                selected_vehicle=data

        if selected_vehicle==None:
            print("Wrong vehicle no, try again")
            continue

        
        try:
            distance= float(input("Enter the travel distance in km: "))
            if distance <=0:
                print("distance must be greater than zero..")
                continue
        except ValueError as e:
            print(e)
            continue
        
        total= distance* selected_vehicle.price_per_km

        print("Your Ride Booke successfully")
        print("="*60)
        print( f"Driver: {selected_vehicle.driver_name}\nVehicle:{selected_vehicle.brand_name}\nVehicle_no:{selected_vehicle.vehicle_no}\nPrice Per KM: ₹{selected_vehicle.price_per_km}/KM\nTotal Fare: ₹{total}")
        print("="*60)
        answer= input("Would you like to book one more trip yes/no: ")
        if answer!="yes":
            print("Thanks for booking an ride")
            break
    else:
        print("vehicle is not available")
        break
