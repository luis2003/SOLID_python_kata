class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor:
    def __init__(self, security_code):
        self.security_code: str = security_code

    def pay_debit(self, an_order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        an_order.status = "paid"

    def pay_credit(self, an_order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        an_order.status = "paid"
