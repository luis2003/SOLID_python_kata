from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, an_order):
        pass


class PaymentProcessorSMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code):
        pass

    @abstractmethod
    def pay(self, an_order):
        pass


class DebitPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, security_code):
        self.security_code: str = security_code
        self.verified = False

    def pay(self, an_order):
        if not self.verified:
            raise Exception("Not authorized")
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


class PayPalPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, email):
        self.verified = False
        self.email: str = email

    def pay(self, an_order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing PayPal payment type")
        print(f"Verifying email: {self.email}")
        an_order.status = "paid"

    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True
