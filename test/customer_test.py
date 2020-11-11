import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jack Sparrow", 1000, 40)

    def test_has_name(self):
        self.assertEqual("Jack Sparrow", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(1000, self.customer.wallet)

    def test_can_pay(self):
        self.customer.pay_bill(100)
        self.assertEqual(900, self.customer.wallet)
