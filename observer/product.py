from .user import User

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
        self.observers = []

    def attach(self, observer: User):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer: User):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if self._price != new_price:
            self._price = new_price
            self.notify()