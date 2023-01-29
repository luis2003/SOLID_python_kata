import unittest
from payment_system.payment_processor import PaymentProcessor
from payment_system.order import Order


class PaymentProcessorTestCase(unittest.TestCase):
    def test_creation(self):
        a_processor = PaymentProcessor("0372846")
        self.assertIsInstance(a_processor, PaymentProcessor)

    def test_pay_debit(self):
        a_processor = PaymentProcessor("0372846")
        an_order = Order()
        a_processor.pay_debit(an_order)
        self.assertEqual("paid", an_order.status)

    def test_pay_credit(self):
        a_processor = PaymentProcessor("0372846")
        an_order = Order()
        a_processor.pay_credit(an_order)
        self.assertEqual("paid", an_order.status)


if __name__ == '__main__':
    unittest.main()
