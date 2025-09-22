from .payment_strategy import PaymentStrategy

class CheckoutService:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount):
        print(f"Processing payment...")
        self.payment_strategy.pay(amount)