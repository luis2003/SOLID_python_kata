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

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


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


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
processor = PaymentProcessor("0372846")
processor.pay_debit(order)
