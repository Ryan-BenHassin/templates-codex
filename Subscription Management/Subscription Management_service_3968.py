class Subscription:
 def __init__(self):
 self.subscriptions = {}

 def create_subscription(self, customer_id, subscription_name, plan):
 if customer_id in self.subscriptions:
 print("Customer already has a subscription.")
 else:
 self.subscriptions[customer_id] = {"subscription_name": subscription_name, "plan": plan}
 print("Subscription created successfully.")

 def edit_subscription(self, customer_id, subscription_name, plan):
 if customer_id in self.subscriptions:
 self.subscriptions[customer_id] = {"subscription_name": subscription_name, "plan": plan}
 print("Subscription updated successfully.")
 else:
 print("Customer does not have a subscription.")

 def cancel_subscription(self, customer_id):
 if customer_id in self.subscriptions:
 del self.subscriptions[customer_id]
 print("Subscription cancelled successfully.")
 else:
 print("Customer does not have a subscription.")

 def view_subscription(self, customer_id):
 if customer_id in self.subscriptions:
 print(f"Subscription Name: {self.subscriptions[customer_id]['subscription_name']}")
 print(f"Plan: {self.subscriptions[customer_id]['plan']}")
 else:
 print("Customer does not have a subscription.")


subscription_management = Subscription()

while True:
 print("\n1. Create Subscription")
 print("2. Edit Subscription")
 print("3. Cancel Subscription")
 print("4. View Subscription")
 print("5. Exit")

 choice = input("Choose an option: ")

 if choice == "1":
 customer_id = input("Enter customer ID: ")
 subscription_name = input("Enter subscription name: ")
 plan = input("Enter plan: ")
 subscription_management.create_subscription(customer_id, subscription_name, plan)
 elif choice == "2":
 customer_id = input("Enter customer ID: ")
 subscription_name = input("Enter subscription name: ")
 plan = input("Enter plan: ")
 subscription_management.edit_subscription(customer_id, subscription_name, plan)
 elif choice == "3":
 customer_id = input("Enter customer ID: ")
 subscription_management.cancel_subscription(customer_id)
 elif choice == "4":
 customer_id = input("Enter customer ID: ")
 subscription_management.view_subscription(customer_id)
 elif choice == "5":
 break
 else:
 print("Invalid option. Please choose a valid option.")
