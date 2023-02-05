import unittest
from payment_system.payment_processor import DebitPaymentProcessor, CreditPaymentProcessor, \
    PayPalPaymentProcessor
from payment_system.order import Order
from payment_system.sms_authorizer import SMSAuthorizer


class PaymentProcessorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.an_sms_auth = SMSAuthorizer()
        self.a_debit_processor = DebitPaymentProcessor("0372846", self.an_sms_auth)
        self.a_credit_processor = CreditPaymentProcessor("0372846")
        self.a_paypal_proc = PayPalPaymentProcessor("name@mailserver.com", self.an_sms_auth)
        self.an_order = Order()

    def test_debit_except_sms_not_verified(self):
        with self.assertRaises(Exception):
            self.a_debit_processor.pay(self.an_order)

    def test_paypal_except_sms_not_verified(self):
        with self.assertRaisesRegex(Exception, "Not authorized"):
            self.a_paypal_proc.pay(self.an_order)

    def test_pay_debit(self):
        self.an_sms_auth.verify_code(123456)
        self.a_debit_processor.pay(self.an_order)
        self.assertEqual("paid", self.an_order.status)

    def test_pay_credit(self):
        self.a_credit_processor.pay(self.an_order)
        self.assertEqual("paid", self.an_order.status)

    def test_pay_paypal(self):
        self.an_sms_auth.verify_code(123456)
        self.a_paypal_proc.pay(self.an_order)
        self.assertEqual("paid", self.an_order.status)


if __name__ == '__main__':
    unittest.main()
