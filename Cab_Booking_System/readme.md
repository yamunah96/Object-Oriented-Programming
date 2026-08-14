# Cab Booking System

A simple Python **Cab Booking System** built using Object-Oriented Programming (OOP) concepts.

The program contains a predefined fleet of **2 Cars and 2 Bikes**. Customers can select a vehicle type, choose an available vehicle, enter the travel distance, and calculate the total fare. The system also supports **multiple trip bookings**.

## Features

* Parent `Vehicle` class for common vehicle information
* Child classes:

  * `Car`
  * `Bike`
* Predefined fleet with:

  * 2 Cars
  * 2 Bikes
* Select a vehicle type
* View available vehicles
* Select a vehicle using its vehicle number
* Enter travel distance
* Calculate total fare
* Handle invalid vehicle numbers
* Handle invalid distance input
* Book multiple trips using a loop

## OOP Concepts Used

### Parent Class: `Vehicle`

The `Vehicle` class contains common information shared by all vehicles:

* Driver Name
* Vehicle Number
* Brand Name
* Price Per KM

These values are stored as instance attributes.

### Child Classes

The program contains two child classes:

```text
Vehicle
├── Car
└── Bike
```

Both `Car` and `Bike` inherit the common properties and methods from the `Vehicle` class.

## Available Fleet

### Cars

| Vehicle Number | Brand         | Driver |  Rate |
| -------------- | ------------- | ------ | ----: |
| KA1234         | Toyota        | Rahul  | ₹8/KM |
| KA2626         | Maruti Suzuki | Yash   | ₹6/KM |

### Bikes

| Vehicle Number | Brand        | Driver |  Rate |
| -------------- | ------------ | ------ | ----: |
| KA7680         | TVS          | Rina   | ₹5/KM |
| KA9090         | Active Honda | Gagan  | ₹6/KM |

## Fare Calculation

The total fare is calculated using the following formula:

```text
Total Fare = Travel Distance × Price Per KM
```

### Example

```text
Travel Distance = 15 KM
Price Per KM = ₹8

Total Fare = 15 × 8
           = ₹120
```

## Program Flow

```text
Start
  ↓
Select Vehicle Type
  ↓
Display Available Vehicles
  ↓
Select Vehicle Number
  ↓
Enter Travel Distance
  ↓
Calculate Total Fare
  ↓
Display Booking Details
  ↓
Book Another Trip?
  ├── Yes → Start New Booking
  └── No  → Exit
```

## Example Output

```text
Enter vehicle type Car/Bike: car

======================================================================

Driver: Rahul
Vehicle: Toyota
Vehicle_no: KA1234
Price Per KM: ₹8/KM

======================================================================

Driver: Yash
Vehicle: Maruti Suzuki
Vehicle_no: KA2626
Price Per KM: ₹6/KM

======================================================================

Enter vehicle_no to book a ride: KA1234
Enter the travel distance in km: 15

Your Ride Booked Successfully

============================================================

Driver: Rahul
Vehicle: Toyota
Vehicle_no: KA1234
Price Per KM: ₹8/KM
Total Fare: ₹120

============================================================

Would you like to book one more trip yes/no:
```

## Project Concepts

This project demonstrates:

* Classes and Objects
* Constructors
* Instance Attributes
* Inheritance
* Parent and Child Classes
* Lists and Dictionaries
* Loops
* Conditional Statements
* Exception Handling
* User Input
* Fare Calculation
* Multiple Trip Booking

## How to Run

1. Save the Python code in a file such as `main.py`.
2. Run the program.
3. Select either `Car` or `Bike`.
4. View the available vehicles.
5. Enter the vehicle number you want to book.
6. Enter the travel distance.
7. View the calculated fare.
8. Choose `yes` to book another trip or `no` to exit.
