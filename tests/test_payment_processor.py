import unittest
from payment_system.payment_processor import PaymentProcessor
from payment_system.order import Order


class PaymentProcessorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.a_processor = PaymentProcessor("0372846")
        self.an_order = Order()

    def test_creation(self):
        self.assertIsInstance(self.a_processor, PaymentProcessor)

    def test_pay_debit(self):
        self.a_processor.pay_debit(self.an_order)
        self.assertEqual("paid", self.an_order.status)

    def test_pay_credit(self):
        self.a_processor.pay_credit(self.an_order)
        self.assertEqual("paid", self.an_order.status)


if __name__ == '__main__':
    unittest.main()
