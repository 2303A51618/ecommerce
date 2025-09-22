class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update(self, product):
        print(f"Notification for {self.name}: The price of {product.name} has dropped to ${product.price}.")