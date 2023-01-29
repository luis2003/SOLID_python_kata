import unittest
from payment_system.order import Order


class OrderTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.an_order = Order()

    @unittest.skip("This test is redundant with SetUp")
    def test_order_creation_ok(self):
        self.assertIsInstance(self.an_order, Order)

    def test_total_price_multiple_items_with_repeated_item(self):
        self.an_order.add_item("Keyboard", 1, 50)
        self.an_order.add_item("SSD", 1, 150)
        self.an_order.add_item("USB cable", 2, 5)
        self.assertEqual(210, self.an_order.total_price())


if __name__ == '__main__':
    unittest.main()
