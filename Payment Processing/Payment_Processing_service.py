import stripe

# Configure your Stripe secret key (ideally should be loaded from a secure environment variable or configuration file)
stripe.api_key = "sk_test_51GWIK4AUEoYEaNjNLciMckn2RJiIk1phq6th4qqT7iwc7j4Hnp07sD22yOJAqbPGgWVhKG0ctOcqJ6mUghBb4OBK00o9067Mmo"

def process_payment(amount, currency, token):
    try:
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Convert amount to cents
            currency=currency,
            source=token,  # Use the token, not the raw card data
            description="Test payment"
        )
        return charge.outcome.seller_message
    except stripe.error.StripeError as e:
        print(f"Error: {str(e)}")
        return "Payment failed: " + str(e.user_message)

def create_customer(email, name, description):
    """Create a new Stripe customer with provided details."""
    try:
        return stripe.Customer.create(email=email, name=name, description=description)
    except stripe.error.StripeError as e:
        print(f"Failed to create customer: {str(e)}")
        return None

def create_payment_method(use_test_token=False, **card_details):
    """Create a Stripe payment method, either using a test token or card details."""
    try:
        if use_test_token:
            return stripe.PaymentMethod.create(type="card", card={"token": "tok_visa"})
        return stripe.PaymentMethod.create(
            type="card",
            card=card_details,
            billing_details={"name": card_details.get('name')}
        )
    except stripe.error.StripeError as e:
        print(f"Failed to create payment method: {str(e)}")
        return None

def attach_payment_method(customer_id, payment_method_id):
    """Attach a payment method to a customer in Stripe."""
    try:
        stripe.PaymentMethod.attach(payment_method_id, customer=customer_id)
        return True
    except stripe.error.StripeError as e:
        print(f"Failed to attach payment method: {str(e)}")
        return False

def create_subscription(customer_id, payment_method_id, price_id):
    """Create a Stripe subscription for a customer using a specified price and payment method."""
    try:
        return stripe.Subscription.create(
            customer=customer_id,
            items=[{"price": price_id}],
            default_payment_method=payment_method_id
        )
    except stripe.error.StripeError as e:
        print(f"Failed to create subscription: {str(e)}")
        return None

def create_payment_intent(customer_id, amount, payment_method_id, currency='usd'):
    """Create and confirm a Stripe payment intent for specified amount and currency."""
    try:
        return stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Convert amount to cents
            currency=currency,
            customer=customer_id,
            payment_method=payment_method_id,
            confirm=True,
            off_session=True  # Set to True if the customer is not present
        )
    except stripe.error.StripeError as e:
        print(f"Failed to create payment intent: {str(e)}")
        return None

def process_payment(amount, currency, token):
    """Process a payment using a charge (deprecated method, use PaymentIntent for new integrations)."""
    try:
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Convert amount to cents
            currency=currency,
            source=token,
            description="Test payment"
        )
        return charge.outcome.seller_message
    except stripe.error.StripeError as e:
        print(f"Error during charge creation: {str(e)}")
        return "Payment failed: " + str(e.user_message)

# Main logic for demonstrating usage
if __name__ == "__main__":
    print(process_payment(10.99, "usd", "tok_visa"))  # Use an actual token received from Stripe's testing documentation

    customer = create_customer("test@example.com", "John Doe", "Test customer")
    if not customer:
        exit("Failed to create customer, stopping script.")
    print("Customer created:", customer.id)
    payment_method = create_payment_method(use_test_token=True)
    if not payment_method:
        exit("Failed to create payment method, stopping script.")
    print("Payment method created:", payment_method.id)

    if not attach_payment_method(customer.id, payment_method.id):
        exit("Failed to attach payment method, stopping script.")

    subscription = create_subscription(customer.id, payment_method.id, "price_1PErB7AUEoYEaNjNa0N6YVMf")
    if not subscription:
        exit("Failed to create subscription, stopping script.")
    print("Subscription created:", subscription.id)
    payment_intent = create_payment_intent(customer.id, 10.99, payment_method.id)
    if not payment_intent:
        exit("Failed to create payment intent, stopping script.")
    print("Payment Intent created:", payment_intent.id)

    print("All operations completed successfully.")
