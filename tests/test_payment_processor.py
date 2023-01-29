import unittest
from payment_system.payment_processor import DebitPaymentProcessor, CreditPaymentProcessor
from payment_system.order import Order


class PaymentProcessorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.a_debit_processor = DebitPaymentProcessor("0372846")
        self.a_credit_processor = CreditPaymentProcessor("0372846")
        self.an_order = Order()

    def test_pay_debit(self):
        self.a_debit_processor.pay(self.an_order)
        self.assertEqual("paid", self.an_order.status)

    def test_pay_credit(self):
        self.a_credit_processor.pay(self.an_order)
        self.assertEqual("paid", self.an_order.status)


if __name__ == '__main__':
    unittest.main()
