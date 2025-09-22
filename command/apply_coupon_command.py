# command/apply_coupon_command.py
from .command import Command
from .cart_service import CartService

class ApplyCouponCommand(Command):
    def __init__(self, cart_service: CartService, coupon):
        self.cart_service = cart_service
        self.coupon = coupon

    def execute(self):
        self.cart_service.apply_coupon(self.coupon)

    def undo(self):
        # In a real-world scenario, this would remove the coupon
        # For simplicity, we'll just print a message
        print(f"Undoing application of coupon '{self.coupon}'")