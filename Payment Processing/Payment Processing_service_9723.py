#TODO
import stripe

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

def create_customer(email, name, description):
 customer = stripe.Customer.create(email=email, name=name, description=description)
 return customer

def create_payment_method(card_number, exp_month, exp_year, cvc, cardholder_name):
 payment_method = stripe.PaymentMethod.create(type="card", card={"number": card_number, "exp_month": exp_month, "exp_year": exp_year, "cvc": cvc, "name": cardholder_name})
 return payment_method

def attach_payment_method(customer_id, payment_method_id):
 stripe.PaymentMethod.attach(payment_method_id, customer=customer_id)

def create_subscription(customer_id, payment_method_id, price_id):
 subscription = stripe.Subscription.create(customer=customer_id, items=[{"price": price_id}], payment_settings={"payment_method_types": ["card"], "payment_method": payment_method_id})
 return subscription

def charge(customer_id, amount):
 charge = stripe.Charge.create(customer=customer_id, amount=amount, currency="usd")
 return charge

# Example usage
customer = create_customer("test@example.com", "John Doe", "Test customer")
payment_method = create_payment_method("4242424242424242", 12, 2025, 123, "John Doe")
attach_payment_method(customer.id, payment_method.id)
subscription = create_subscription(customer.id, payment_method.id, "YOUR_STRIPE_PRICE_ID")
charge(customer.id, 1000)

print("Customer created:", customer)
print("Payment method created:", payment_method)
print("Subscription created:", subscription)
print("Charge created:", charge)
