import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Rum", 5, 2)

    def test_has_name(self):
        self.assertEqual("Rum", self.drink.name)

    def test_has_price(self):
        self.assertEqual(5, self.drink.price)
