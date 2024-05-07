import stripe

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

def create_customer(email, payment_method):
 try:
 customer = stripe.Customer.create(email=email, payment_method=payment_method)
 return customer.id
 except stripe.error.CardError as e:
 return str(e)

def create_payment_method(card_number, exp_month, exp_year, cvc):
 try:
 payment_method = stripe.PaymentMethod.create(
 type="card",
 card={
 "number": card_number,
 "exp_month": exp_month,
 "exp_year": exp_year,
 "cvc": cvc
 }
 )
 return payment_method.id
 except stripe.error.CardError as e:
 return str(e)

def create_subscription(customer_id, price_id):
 try:
 subscription = stripe.Subscription.create(
 customer=customer_id,
 items=[{"price": price_id}],
 payment_method="pm_card_visa"
 )
 return subscription.id
 except stripe.error.CardError as e:
 return str(e)

def make_payment(customer_id, amount, currency):
 try:
 payment_intent = stripe.PaymentIntent.create(
 amount=amount,
 currency=currency,
 setup_future_usage="off_session",
 customer=customer_id
 )
 return payment_intent.id
 except stripe.error.CardError as e:
 return str(e)

# Example usage:
email = "example@example.com"
card_number = "4242424242424242"
exp_month = 12
exp_year = 2025
cvc = "123"
customer_id = create_customer(email, "pm_card_visa")
payment_method_id = create_payment_method(card_number, exp_month, exp_year, cvc)
subscription_id = create_subscription(customer_id, "price_1KKN07BTIh8RqU4PSPXk6wAq")
payment_id = make_payment(customer_id, 1000, "usd")
print("Customer ID:", customer_id)
print("Payment Method ID:", payment_method_id)
print("Subscription ID:", subscription_id)
print("Payment ID:", payment_id)
