from payment_system.payment_processor import PaymentProcessor, PayPalPaymentProcessor
from payment_system.order import Order


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)
    print(order.total_price())
    processor = PayPalPaymentProcessor("name@mailserver.com")
    processor.auth_sms(12345)
    processor.pay(order)


if __name__ == '__main__':
    main()
