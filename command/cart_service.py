class CartService:
    def __init__(self):
        self.items = []
        self.coupons = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added '{item}' to cart. Current items: {self.items}")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed '{item}' from cart. Current items: {self.items}")

    def apply_coupon(self, coupon_code):
        self.coupons.append(coupon_code)
        print(f"Applied coupon '{coupon_code}'.")