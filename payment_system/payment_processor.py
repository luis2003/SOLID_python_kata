from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def auth_sms(self, code):
        pass

    @abstractmethod
    def pay(self, an_order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code: str = security_code
        self.verified = False

    def pay(self, an_order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        an_order.status = "paid"

    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code: str = security_code

    def pay(self, an_order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        an_order.status = "paid"

    def auth_sms(self, param):
        pass


class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email: str = email

    def pay(self, an_order):
        print("Processing PayPal payment type")
        print(f"Verifying email: {self.email}")
        an_order.status = "paid"

    def auth_sms(self, param):
        pass
