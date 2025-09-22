 #strategy/wallet_payment.py
from .payment_strategy import PaymentStrategy

class WalletPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using Wallet.")
        # Logic for wallet payment processing
