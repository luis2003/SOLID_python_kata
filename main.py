from payment_system.sms_authorizer import SMSAuthorizer
from payment_system.payment_processor import PayPalPaymentProcessor
from payment_system.order import Order


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)
    print(order.total_price())
    sms_auth = SMSAuthorizer()
    processor = PayPalPaymentProcessor("name@mailserver.com", sms_auth)
    sms_auth.verify_code(12345)
    processor.pay(order)


if __name__ == '__main__':
    main()
