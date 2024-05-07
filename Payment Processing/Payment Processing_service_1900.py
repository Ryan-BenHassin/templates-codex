#TODO
import stripe

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

def process_payment(amount, currency, card_number, exp_month, exp_year, cvc):
    try:
        token = stripe.Token.create(
            card={
                "number": card_number,
                "exp_month": exp_month,
                "exp_year": exp_year,
                "cvc": cvc
            }
        )
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Convert amount to cents
            currency=currency,
            source=token.id,
            description="Test payment"
        )
        return charge.outcome.seller_message
    except stripe.error.CardError as e:
        return e.user_message

print(process_payment(10.99, "usd", "4242424242424242", 12, 2025, 123))