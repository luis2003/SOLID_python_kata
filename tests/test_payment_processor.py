import unittest
from payment_system.payment_processor import DebitPaymentProcessor, CreditPaymentProcessor, PayPalPaymentProcessor
from payment_system.order import Order


class PaymentProcessorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.a_debit_processor = DebitPaymentProcessor("0372846")
        self.a_credit_processor = CreditPaymentProcessor("0372846")
        self.a_paypal_proc = PayPalPaymentProcessor("name@mailserver.com")
        self.an_order = Order()

    def test_debit_auth_sms(self):
        self.a_debit_processor.auth_sms("a_valid_code")
        self.assertTrue(self.a_debit_processor.verified)

    def test_paypal_auth_sms(self):
        self.a_paypal_proc.auth_sms(43435)
        self.assertTrue(self.a_paypal_proc.verified)

    def test_pay_debit(self):
        self.a_debit_processor.pay(self.an_order)
        self.assertEqual("paid", self.an_order.status)

    def test_pay_credit(self):
        self.a_credit_processor.pay(self.an_order)
        self.assertEqual("paid", self.an_order.status)

    def test_pay_paypal(self):
        self.a_paypal_proc.pay(self.an_order)
        self.assertEqual("paid", self.an_order.status)


if __name__ == '__main__':
    unittest.main()
