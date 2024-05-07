import datetime

class Subscription:
 def __init__(self, customer_id, subscription_id, service, start_date, end_date):
 self.customer_id = customer_id
 self.subscription_id = subscription_id
 self.service = service
 self.start_date = start_date
 self.end_date = end_date

class SubscriptionManagement:
 def __init__(self):
 self.subscriptions = []

 def add_subscription(self, customer_id, subscription_id, service, start_date, end_date):
 subscription = Subscription(customer_id, subscription_id, service, start_date, end_date)
 self.subscriptions.append(subscription)

 def get_subscriptions(self, customer_id):
 return [subscription for subscription in self.subscriptions if subscription.customer_id == customer_id]

 def cancel_subscription(self, subscription_id):
 self.subscriptions = [subscription for subscription in self.subscriptions if subscription.subscription_id != subscription_id]

 def renew_subscription(self, subscription_id, new_end_date):
 for subscription in self.subscriptions:
 if subscription.subscription_id == subscription_id:
 subscription.end_date = new_end_date
 break

subscription_management = SubscriptionManagement()

while True:
 print("1. Add subscription")
 print("2. Get subscriptions")
 print("3. Cancel subscription")
 print("4. Renew subscription")
 print("5. Exit")
 choice = input("Choose an option: ")

 if choice == "1":
 customer_id = input("Enter customer ID: ")
 subscription_id = input("Enter subscription ID: ")
 service = input("Enter service: ")
 start_date = datetime.datetime.now()
 end_date = datetime.datetime.now() + datetime.timedelta(days=30)
 subscription_management.add_subscription(customer_id, subscription_id, service, start_date, end_date)
 elif choice == "2":
 customer_id = input("Enter customer ID: ")
 subscriptions = subscription_management.get_subscriptions(customer_id)
 for subscription in subscriptions:
 print(f"Subscription ID: {subscription.subscription_id}, Service: {subscription.service}, Start Date: {subscription.start_date}, End Date: {subscription.end_date}")
 elif choice == "3":
 subscription_id = input("Enter subscription ID: ")
 subscription_management.cancel_subscription(subscription_id)
 elif choice == "4":
 subscription_id = input("Enter subscription ID: ")
 end_date = datetime.datetime.now() + datetime.timedelta(days=30)
 subscription_management.renew_subscription(subscription_id, end_date)
 elif choice == "5":
 break
 else:
 print("Invalid option. Please choose a valid option.")
