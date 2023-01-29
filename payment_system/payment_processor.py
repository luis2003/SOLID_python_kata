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
