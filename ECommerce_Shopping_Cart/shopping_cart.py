class Product:
    def __init__(self,product_id,product_name,category,price,available_stock):
        self.product_id=product_id
        self.product_name=product_name
        self.category=category
        self.price=price
        self.available_stock=available_stock
    def display(self):
        return f"Product: {self.product_name}\nPrice:{self.price}"

class Shopping_Cart:
    def __init__(self):
        self.cart_data=[]

    def check_stock(self,product,quantity):
        if quantity<=product.available_stock:
            return True
        
    def add_products(self,product,quantity):
        if self.check_stock(product,quantity):
            for item in self.cart_data:
                if item["product"]==product:
                    item['quantity']+=quantity
                    product.available_stock-=quantity
                    print("Product quantity updated in cart.")
                    return
        
            self.cart_data.append(
                {
                    "product":product,
                    "quantity":quantity
                }
            )
            product.available_stock-=quantity
            print("Product Added to cart")
        else:
            print(f"There are only {product.available_stock} is available in stock")

    def remove_products(self,product,quantity):
        for item in self.cart_data:
            product=item["product"]
            if product.product_name.lower() == product_name.lower():
                if quantity>=item["quantity"]:
                    product.available_stock+=item["quantity"]
                    self.cart_data.remove(item)
                    print("Product removed from the cart")
                else:
                    item["quantity"]-=quantity
                    product.available_stock+=item["quantity"]
                    print("Product Quantity updated")
                return
        print("Product not found in cart")


    
    def display_cart_products(self):
        if not self.cart_data:
            print("Your cart is empty")
            return

        print("===============Cart====================")
        for item in self.cart_data:
            # print(item)
            product=item['product']
            quantity=item["quantity"]
            print(f"Product: {product.product_name}\nPrice: ₹{product.price}\nQuantity: {quantity}\nSubtotal: ₹{product.price*quantity}")
            print(" ")

    def calculate_total(self):
        total=0
        for item in self.cart_data:
            product=item['product']
            quantity=item["quantity"]
            total+=product.price*quantity
        return f"Total: {total}"

    

p1=Product("p1","Vim Soap","Kitchen",10,10)
p2=Product("p2","Detol Handwash","Kitchen",35,5)
p3=Product("p3","Amul Paneer","Food",110,4)
p4=Product("p4","Protein Bar","Food",47,9)
p5=Product("p5","Headphone","Electronics",1500,0)
products_data={
    "kitchen":[p1,p2],
    "food":[p3,p4],
    "electronics":[p5]
}
cart_item=Shopping_Cart()

while True:
    print("===============Available Products ==================")
    for products in products_data.values():
        for product in products:
            print(product.product_name)
    print("="*60)
    print(" ")
    print(f"1.Add Product\n2.Remove Product\n3.Display Cart\n4.Exit")
    try:
        choice=int(input("Select an option: "))

        # add Product 
        if choice ==1:
            product_name= input("Enter the product name: ").lower().strip()
            selected_product = None

            for products in products_data.values():
                for product in products:
                    if product_name == product.product_name.lower():
                        selected_product=product
                        break
                if selected_product:
                    break

            if selected_product:
                if selected_product.available_stock==0:
                    print(f"{selected_product.product_name} is out of stock")
                    continue

                print('Product Found.........')
                print(selected_product.display())

                try:
                    quantity=int(input("Enter quantity: "))
                    if quantity<0:
                        print("quantity must be greater than zero")
                    else:
                        cart_item.add_products(selected_product,quantity)
                except ValueError:
                    print("Enter the valid number")
            else:
                print("Product Not Found")

        # Remove product
        elif choice==2:
            product_name= input("Enter the product name: ").lower().strip()
            try:
                quantity=int(input("Enter quantity: "))
                if quantity>0:
                    cart_item.remove_products(product_name,quantity)
                else:
                    cart_item.add_products(selected_product,quantity)
            except ValueError:
                print("Enter the valid number")

        # display cart products
        elif choice==3:
            cart_item.display_cart_products()
            print(cart_item.calculate_total())
        elif choice==4:
            print("Thanks for visting")
            break
        else:
            print("Invalid choice,Try again")
    except ValueError:
        print("Enter the valid choice")
