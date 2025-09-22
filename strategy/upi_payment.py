# strategy/upi_payment.py
from .payment_strategy import PaymentStrategy

class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using UPI.")
        # Logic for UPI payment processing
