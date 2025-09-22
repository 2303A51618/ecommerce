# strategy/card_payment.py
from .payment_strategy import PaymentStrategy

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using Credit/Debit Card.")
        # Logic for card payment processing
