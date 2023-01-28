import unittest
from single_responsibility import PaymentProcessor


class PaymentProcessor_TestCase(unittest.TestCase):
    def test_payment_processor_creation(self):
        a_processor = PaymentProcessor()
        self.assertIsInstance(a_processor, PaymentProcessor)


if __name__ == '__main__':
    unittest.main()
