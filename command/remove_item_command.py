# command/remove_item_command.py
from .command import Command
from .cart_service import CartService

class RemoveItemCommand(Command):
    def __init__(self, cart_service: CartService, item):
        self.cart_service = cart_service
        self.item = item

    def execute(self):
        self.cart_service.remove_item(self.item)
    
    def undo(self):
        self.cart_service.add_item(self.item)