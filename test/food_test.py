import unittest

from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Fish", 10, 5)

    def test_has_name(self):
        self.assertEqual("Fish", self.food.name)

    def test_has_price(self):
        self.assertEqual(10, self.food.price)