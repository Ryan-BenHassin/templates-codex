class Product:
 def __init__(self, name, price, quantity):
 self.name = name
 self.price = price
 self.quantity = quantity

class Inventory:
 def __init__(self):
 self.products = []

 def add_product(self, product):
 self.products.append(product)

 def remove_product(self, product_name):
 self.products = [product for product in self.products if product.name!= product_name]

 def update_product_quantity(self, product_name, new_quantity):
 for product in self.products:
 if product.name == product_name:
 product.quantity = new_quantity
 return
 print("Product not found")

 def get_product(self, product_name):
 for product in self.products:
 if product.name == product_name:
 return product
 return None

 def display_inventory(self):
 for product in self.products:
 print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")


def main():
 inventory = Inventory()

 while True:
 print("\n1. Add Product")
 print("2. Remove Product")
 print("3. Update Product Quantity")
 print("4. Get Product")
 print("5. Display Inventory")
 print("6. Exit")

 choice = input("Choose an option: ")

 if choice == "1":
 name = input("Enter product name: ")
 price = float(input("Enter product price: "))
 quantity = int(input("Enter product quantity: "))
 product = Product(name, price, quantity)
 inventory.add_product(product)
 elif choice == "2":
 name = input("Enter product name: ")
 inventory.remove_product(name)
 elif choice == "3":
 name = input("Enter product name: ")
 quantity = int(input("Enter new quantity: "))
 inventory.update_product_quantity(name, quantity)
 elif choice == "4":
 name = input("Enter product name: ")
 product = inventory.get_product(name)
 if product:
 print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
 else:
 print("Product not found")
 elif choice == "5":
 inventory.display_inventory()
 elif choice == "6":
 break
 else:
 print("Invalid option")


if __name__ == "__main__":
 main()
