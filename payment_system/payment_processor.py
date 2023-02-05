from abc import ABC, abstractmethod
from payment_system.sms_authorizer import Authorizer


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, an_order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code: str = security_code
        self._authorizer = authorizer

    def pay(self, an_order):
        if not self._authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        an_order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code: str = security_code

    def pay(self, an_order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        an_order.status = "paid"


class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email, authorizer: Authorizer):
        self._authorizer = authorizer
        self.email: str = email

    def pay(self, an_order):
        if not self._authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing PayPal payment type")
        print(f"Verifying email: {self.email}")
        an_order.status = "paid"

