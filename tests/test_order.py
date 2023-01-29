import unittest
from payment_system.order import Order


class OrderTestCase(unittest.TestCase):
    def test_order_creation_ok(self):
        an_order = Order()
        self.assertIsInstance(an_order, Order)


if __name__ == '__main__':
    unittest.main()
