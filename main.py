from single_responsibility import Order, PaymentProcessor


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)
    print(order.total_price())
    processor = PaymentProcessor("0372846")
    processor.pay_debit(order)


if __name__ == '__main__':
    main()
