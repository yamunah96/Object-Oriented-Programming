# Simple Cab Booking System

A simple Python project that simulates a **Cab Booking System** using Object-Oriented Programming (OOP) concepts.

## Features

* Select a vehicle type: **Car** or **Bike**
* Enter vehicle number
* Enter driver name
* Enter vehicle brand
* Enter travel distance
* Automatically calculate the total fare
* Display booking details

## OOP Concepts Used

### Parent Class: `Vehicle`

The `Vehicle` class contains common information shared by both Car and Bike:

* Vehicle Number
* Brand Name
* Driver Name
* Travel Distance

It also contains methods to:

* Calculate the total fare
* Display booking details

### Child Classes

Two child classes inherit from the `Vehicle` class:

* `Car`
* `Bike`

Each vehicle type has a fixed price per kilometer:

| Vehicle | Price per KM |
| ------- | -----------: |
| Car     |          ₹10 |
| Bike    |           ₹5 |

## Fare Calculation

The total fare is calculated using:

```text
Total Fare = Distance × Price Per KM
```

For example:

```text
Distance = 10 KM
Car Rate = ₹10/KM

Total Fare = 10 × 10 = ₹100
```

## How to Run

1. Run the Python file.
2. Select either `Car` or `Bike`.
3. Enter the required vehicle and travel details.
4. The program will calculate and display the total fare.

## Example Output

```text
Select the vehicle Car/Bike: car
Enter the vehicle no: KA01AB1234
Enter the driver name: Rahul
Enter car brand name: Toyota
Enter travel distance in KM: 15

Your Cab has booked successfully.. Enjoy the ride
Driver: Rahul
Distance: 15.0 KM
Rate: ₹10/KM
Total Fare: ₹150.0
```

## Project Structure

```text
Cab Booking System
│
├── Vehicle
│   ├── vehicle_no
│   ├── brand_name
│   ├── driver_name
│   ├── distance
│   ├── calculate_fare()
│   └── display()
│
├── Car
│   └── price_per_km = ₹10
│
└── Bike
    └── price_per_km = ₹5
```

## Concepts Practiced

* Classes and Objects
* Constructors
* Inheritance
* Instance Attributes
* Class Attributes
* Methods
* Exception Handling
* User Input
