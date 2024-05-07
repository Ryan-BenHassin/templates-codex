#TODO
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

 def remove_product(self, name):
 for product in self.products:
 if product.name == name:
 self.products.remove(product)
 return
 print("Product not found")

 def update_productQuantity(self, name, quantity):
 for product in self.products:
 if product.name == name:
 product.quantity = quantity
 return
 print("Product not found")

 def get_product(self, name):
 for product in self.products:
 if product.name == name:
 return product
 return None

 def list_products(self):
 for product in self.products:
 print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

def main():
 inventory = Inventory()

 while True:
 print("\nOptions:")
 print("1. Add product")
 print("2. Remove product")
 print("3. Update product quantity")
 print("4. Get product")
 print("5. List products")
 print("6. Exit")

 option = input("Choose an option: ")

 if option == "1":
 name = input("Enter product name: ")
 price = float(input("Enter product price: "))
 quantity = int(input("Enter product quantity: "))
 product = Product(name, price, quantity)
 inventory.add_product(product)
 elif option == "2":
 name = input("Enter product name: ")
 inventory.remove_product(name)
 elif option == "3":
 name = input("Enter product name: ")
 quantity = int(input("Enter new quantity: "))
 inventory.update_productQuantity(name, quantity)
 elif option == "4":
 name = input("Enter product name: ")
 product = inventory.get_product(name)
 if product:
 print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
 else:
 print("Product not found")
 elif option == "5":
 inventory.list_products()
 elif option == "6":
 break
 else:
 print("Invalid option")

if __name__ == "__main__":
 main()
