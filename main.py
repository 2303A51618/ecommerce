from observer.product import Product
from observer.user import User
from strategy.checkout_service import CheckoutService
from strategy.card_payment import CardPayment
from strategy.upi_payment import UPIPayment
from strategy.wallet_payment import WalletPayment
from command.cart_service import CartService
from command.add_item_command import AddItemCommand
from command.remove_item_command import RemoveItemCommand
from command.apply_coupon_command import ApplyCouponCommand
from command.invoker import Invoker

def run_observer_demo():
    print("--- Observer Pattern Demo ---")
    iphone = Product("iPhone 15", 999.00)
    user1 = User("Alice", "alice@example.com")
    user2 = User("Bob", "bob@example.com")

    iphone.attach(user1)
    iphone.attach(user2)

    print("Initial price of iPhone is $999.00.")
    print("Changing price to $899.00...")
    iphone.price = 899.00
    print("-" * 25)

def run_strategy_demo():
    print("--- Strategy Pattern Demo ---")
    card_strategy = CardPayment()
    upi_strategy = UPIPayment()
    wallet_strategy = WalletPayment()

    checkout = CheckoutService(card_strategy)
    checkout.process_payment(150.00)

    print("User switches to UPI payment.")
    checkout.set_payment_strategy(upi_strategy)
    checkout.process_payment(200.00)

    print("User switches to Wallet payment.")
    checkout.set_payment_strategy(wallet_strategy)
    checkout.process_payment(75.50)
    print("-" * 25)

def run_command_demo():
    print("--- Command Pattern Demo ---")
    cart = CartService()
    invoker = Invoker()

    add_item1_cmd = AddItemCommand(cart, "Laptop")
    add_item2_cmd = AddItemCommand(cart, "Mouse")
    apply_coupon_cmd = ApplyCouponCommand(cart, "SAVE20")

    invoker.execute_command(add_item1_cmd)
    invoker.execute_command(add_item2_cmd)
    invoker.execute_command(apply_coupon_cmd)

    print("\nAttempting to undo last action...")
    invoker.undo_last_command() # Undoes apply coupon
    
    print("\nAttempting to undo another action...")
    invoker.undo_last_command() # Undoes adding the mouse
    print("-" * 25)

if __name__ == "__main__":
    run_observer_demo()
    run_strategy_demo()
    run_command_demo()