# Online Food Ordering System

## Project Overview

This project is a simple **Online Food Ordering System** built using **Object-Oriented Programming (OOP) in Python**.

The program allows users to:

* Create restaurants
* Add food items to restaurant menus
* Create customers
* Create orders for different customers
* Add multiple food items to an order
* Calculate the total bill
* Display restaurant menus
* Display complete order summaries

The project demonstrates how different Python classes can interact with each other to represent a real-world food ordering system.

---

## OOP Classes Used

### 1. `Resturant`

The `Resturant` class represents a restaurant.

#### Attributes

* `resturant_name` – Name of the restaurant
* `menu` – A list that stores available food items

#### Methods

* `add_food_item(food_item)` – Adds a food item to the restaurant menu
* `display_menu()` – Displays all food items available in the restaurant

---

### 2. `FoodItems`

The `FoodItems` class represents an individual food item.

#### Attributes

* `food_name` – Name of the food
* `category` – Category of the food
* `price` – Price of the food item

#### Methods

* `display()` – Displays the food item's name, category, and price

Example:

```text
Margherita Pizza (Main course) - ₹250
```

---

### 3. `Customer`

The `Customer` class represents a customer who places an order.

#### Attributes

* `customer_id` – Unique ID of the customer
* `name` – Name of the customer

---

### 4. `Orders`

The `Orders` class represents an order placed by a customer.

#### Attributes

* `order_id` – Unique ID of the order
* `customer` – Customer object who placed the order
* `resturant` – Restaurant object from which the order is placed
* `items` – List of food items added to the order

#### Methods

* `add_item(food_item)` – Adds a food item to the order
* `calculate_total()` – Calculates the total price of all ordered items
* `disply_order_summary()` – Displays the complete order summary

---

## Food Items

The following food items are created in the program:

| Food Item        | Category    | Price |
| ---------------- | ----------- | ----: |
| Margherita Pizza | Main course |  ₹250 |
| Masala Dose      | Main course |  ₹100 |
| Ghee Pudi Idli   | Main course |   ₹50 |
| Filter Coffe     | Beverages   |   ₹25 |
| Tiramisu         | Dessert     |  ₹220 |

---

## Restaurants

### Silla Caffe

Menu includes:

* Margherita Pizza
* Masala Dose
* Filter Coffe

### Bangalore Caffee

Menu includes:

* Masala Dose
* Ghee Pudi Idli
* Filter Coffe

---

## Customer Orders

### Order 1

**Customer:** Rahul
**Restaurant:** Silla Caffe

Ordered items:

* Margherita Pizza – ₹250
* Ghee Pudi Idli – ₹50
* Filter Coffe – ₹25

**Total Bill: ₹325**

---

### Order 2

**Customer:** Tina
**Restaurant:** Bangalore Caffee

Ordered item:

* Masala Dose – ₹100

**Total Bill: ₹100**

---

## Project Structure

```text
Online-Food-Ordering-System/
│
├── main.py
└── README.md
```

---

## How to Run the Project

1. Make sure Python is installed on your system.
2. Save the Python code in a file named:

```text
main.py
```

3. Open the terminal in the project folder.
4. Run the following command:

```bash
python main.py
```

---

## Sample Output

```text
===========Silla Caffe Menu===============
Margherita Pizza (Main course) - ₹250
Masala Dose (Main course) - ₹100
Filter coffe (Beverages) - ₹25

===========Bangalore Caffee Menu===============
Masala Dose (Main course) - ₹100
Ghee Pudi idli (Main course) - ₹50
Filter coffe (Beverages) - ₹25

========================================
Order id :1
Customer: Rahul
Resturant: Silla Caffe
Ordered Items:
Margherita Pizza (Main course) - ₹250
Ghee Pudi idli (Main course) - ₹50
Filter coffe (Beverages) - ₹25
==================================================
Total: ₹325
==================================================
```

---

## OOP Concepts Demonstrated

### Classes and Objects

The project creates classes such as:

* `Resturant`
* `FoodItems`
* `Customer`
* `Orders`

Objects are created from these classes to represent real-world entities.

### Encapsulation

Each class combines related data and methods.

For example, the `FoodItems` class stores food information and also provides a `display()` method.

### Object Relationships

The classes interact with each other:

```text
Restaurant
    │
    ├── Food Items
    │
Customer
    │
    └── Order
          │
          ├── Restaurant
          └── Multiple Food Items
```

### Composition

An `Orders` object contains multiple `FoodItems` objects.

```python
order1.add_item(pizza)
order1.add_item(idli)
order1.add_item(coffe)
```

This allows a customer to add multiple items to a single order.
