'''

Build a small Online Food Ordering System using OOP.
Create appropriate classes to represent a restaurant, food items, customers, and orders. 
Your program should allow you to create food items with a name, category, and price; 
create a customer; add multiple food items to an order; calculate the total bill; 
and display the complete order summary.

Create at least 5 food items and demonstrate at least 2 different customer orders.
'''

class Resturant:
    def __init__(self,resturant_name):
        self.resturant_name= resturant_name
        self.menu=[]

    def add_food_item(self,food_item):
        self.menu.append(food_item)

    def display_menu(self):
        print(f"==========={self.resturant_name} Menu===============")
        for item in self.menu:
            item.display()

class FoodItems:
    def __init__(self,food_name,category,price):
        self.food_name= food_name
        self.category=category
        self.price= price

    def display(self):
        print(f"{self.food_name} ({self.category}) - ₹{self.price}")

class Customer:
    def __init__(self,customer_id,name):
        self.customer_id=customer_id
        self.name=name

class Orders:
    def __init__(self,order_id,customer,resturant):
        self.order_id=order_id
        self.customer=customer
        self.resturant= resturant
        self.items=[]

    
    def add_item(self,food_item):
        self.items.append(food_item)

    def calculate_total(self):
        total=0
        for item in self.items:
            total+=item.price
        return total
    def disply_order_summary(self):
        print("="*40)
        print(f"Order id :{self.order_id}\nCustomer: {self.customer.name}\nResturant:{self.resturant.resturant_name}")
        print("Ordered Items: ")
        for item in self.items:
            print(f"{item.food_name} ({item.category}) -₹{item.price}")

        print("="*50)
        print(f"Total: ₹{self.calculate_total()}")
        print("="*50)
# resturant
resturant1= Resturant("Silla Caffe")
resturant2= Resturant("Bangalore Caffee")

# 5 food items
pizza= FoodItems("Margherita Pizza","Main course",250)
dose= FoodItems("Masala Dose","Main course",100)
idli= FoodItems("Ghee Pudi idli","Main course",50)
coffe= FoodItems("Filter coffe","Beverages",25)
tiramisu= FoodItems("Tiramisu","Dessert",220)

resturant1.add_food_item(pizza)
resturant1.add_food_item(dose)
resturant1.add_food_item(coffe)

resturant1.display_menu()

resturant2.add_food_item(dose)
resturant2.add_food_item(idli)
resturant2.add_food_item(coffe)
resturant2.display_menu()

customer1= Customer(101,"Rahul")
customer2=Customer(102,"tina")


order1=Orders(1,customer1,resturant1)
order1.add_item(pizza)
order1.add_item(idli)
order1.add_item(coffe)

order1.disply_order_summary()

order2=Orders(2,customer2,resturant2)
order2.add_item(dose)
order2.disply_order_summary()

