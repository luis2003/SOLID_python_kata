from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    def __init__(self, security_code):
        self.security_code: str = security_code

    @abstractmethod
    def pay(self, an_order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, an_order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        an_order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, an_order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        an_order.status = "paid"
