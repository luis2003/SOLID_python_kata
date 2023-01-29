import unittest
from single_responsibility import PaymentProcessor, Order


class PaymentProcessor_TestCase(unittest.TestCase):
    def test_creation(self):
        a_processor = PaymentProcessor("0372846")
        self.assertIsInstance(a_processor, PaymentProcessor)

    def test_pay_debit(self):
        a_processor = PaymentProcessor("0372846")
        an_order = Order()
        a_processor.pay_debit(an_order)
        self.assertEqual("paid", an_order.status)


if __name__ == '__main__':
    unittest.main()
