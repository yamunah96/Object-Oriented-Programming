## E-Commerce Shopping Cart System

A simple Python project that demonstrates **Object-Oriented Programming (OOP)** by building a basic E-Commerce Shopping Cart System.

## 📌 Project Features

- Create multiple products with different details.
- Add products to the shopping cart.
- Add multiple quantities of a product.
- Update product quantity if the same product is added again.
- Remove products from the cart.
- Display all products in the cart.
- Calculate the total shopping amount.
- Check product availability before adding it to the cart.
- Prevent customers from purchasing products that are out of stock.
- Update available stock when products are added or removed.

---

## Classes

### Product

The `Product` class stores information about each product.

Each product contains:

- Product ID
- Product Name
- Category
- Price
- Available Stock

Example:

```python
p1 = Product("p1", "Vim Soap", "Kitchen", 10, 10)
````

---

### Shopping_Cart

The `Shopping_Cart` class manages the products selected by the customer.

It contains the following methods:

* `check_stock()` – Checks whether the requested quantity is available.
* `add_products()` – Adds a product to the cart.
* `remove_products()` – Removes a product or reduces its quantity.
* `display_cart_products()` – Displays all products in the cart.
* `calculate_total()` – Calculates the total price of all cart items.

---

## Available Products

The program contains five products:

| Product         | Category    | Price | Stock |
| --------------- | ----------- | ----: | ----: |
| Vim Soap        | Kitchen     |   ₹10 |    10 |
| Dettol Handwash | Kitchen     |   ₹35 |     5 |
| Amul Paneer     | Food        |  ₹110 |     4 |
| Protein Bar     | Food        |   ₹47 |     9 |
| Headphone       | Electronics | ₹1500 |     0 |

---

## How the Shopping Cart Works

1. The program displays the available products.
2. The customer selects an option from the menu.
3. The customer can add a product by entering its name and quantity.
4. The program checks whether the product is available in stock.
5. If the requested quantity is available, the product is added to the cart.
6. The available stock is reduced after adding the product.
7. If the same product is added again, its quantity is updated in the cart.
8. The customer can remove products from the cart.
9. The customer can display all selected products.
10. The program calculates the total amount of all cart items.

---

## Out of Stock Handling

The program prevents customers from purchasing products with zero stock.

For example:

```python
p5 = Product("p5", "Headphone", "Electronics", 1500, 0)
```

If the customer tries to purchase this product, the program displays:

```text
Headphone is out of stock
```

The product will not be added to the shopping cart.

---

## Example Cart

```text
===============Cart====================

Product: Vim Soap
Price: ₹10
Quantity: 2
Subtotal: ₹20

Product: Protein Bar
Price: ₹47
Quantity: 3
Subtotal: ₹141

Total: 161
```

---

## OOP Concepts Used

This project demonstrates:

* Classes and Objects
* Constructors
* Instance Attributes
* Instance Methods
* Encapsulation
* Object Interaction

### Project Structure

```text
Product
│
├── product_id
├── product_name
├── category
├── price
└── available_stock


Shopping_Cart
│
├── cart_data
│
├── check_stock()
├── add_products()
├── remove_products()
├── display_cart_products()
└── calculate_total()
```

---

## How to Run

Save the program as:

```text
shopping_cart.py
```

Run the program using:

```bash
python shopping_cart.py
```

---


