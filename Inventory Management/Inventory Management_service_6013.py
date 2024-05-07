#TODO
class InventoryManagement:
 def __init__(self):
 self.items = {}

 def add_item(self, item_name, quantity):
 if item_name in self.items:
 self.items[item_name] += quantity
 else:
 self.items[item_name] = quantity

 def remove_item(self, item_name, quantity):
 if item_name in self.items:
 if self.items[item_name] > quantity:
 self.items[item_name] -= quantity
 else:
 del self.items[item_name]
 else:
 print("Item not found in inventory")

 def check_availability(self, item_name):
 if item_name in self.items:
 return self.items[item_name]
 else:
 return 0

 def list_items(self):
 for item, quantity in self.items.items():
 print(f"Item: {item}, Quantity: {quantity}")


def main():
 inventory = InventoryManagement()
 while True:
 print("1. Add item to inventory")
 print("2. Remove item from inventory")
 print("3. Check item availability")
 print("4. List all items")
 print("5. Exit")
 choice = input("Choose an option: ")
 if choice == "1":
 item_name = input("Enter item name: ")
 quantity = int(input("Enter quantity: "))
 inventory.add_item(item_name, quantity)
 elif choice == "2":
 item_name = input("Enter item name: ")
 quantity = int(input("Enter quantity: "))
 inventory.remove_item(item_name, quantity)
 elif choice == "3":
 item_name = input("Enter item name: ")
 availability = inventory.check_availability(item_name)
 print(f"Availability: {availability}")
 elif choice == "4":
 inventory.list_items()
 elif choice == "5":
 break
 else:
 print("Invalid option. Please choose again.")


if __name__ == "__main__":
 main()
