import unittest

from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food 

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Rusty Screw", 100)
        self.customer = Customer("Jack Sparrow", 1000, 20)
        self.drink = Drink("Rum", 5, 2)
        self.drink_2 = Drink("Rum n coke", 7, 5)
        self.food = Food("Fish", 10, 1)

    def test_has_name(self):
        self.assertEqual("The Rusty Screw", self.pub.name)

    def test_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_can_increase(self):
        self.pub.increase_till(100)
        self.assertEqual(200, self.pub.till)

    def test_can_buy_drink(self):
        self.pub.sell_customer_drink(self.customer, self.drink)
        self.assertEqual(105, self.pub.till)
        self.assertEqual(995, self.customer.wallet)

    def test_check_cust_is_over18(self):
        is_true = self.pub.check_age(self.customer)
        self.assertEqual(True, is_true)

    def test_check_cust_is_under18(self):
        self.customer_2 = Customer("Billy the kid", 500, 17)
        is_false = self.pub.check_age(self.customer_2)
        self.assertEqual(False, is_false)

    def test_check_customer_is_getting_smashed(self):
        self.pub.sell_customer_drink(self.customer, self.drink)
        self.assertEqual(2, self.customer.drunkenness)
    
    def test_if_customer_is_too_drunk(self):
        self.pub.sell_customer_drink(self.customer, self.drink_2)
        can_buy = self.pub.sell_customer_drink(self.customer, self.drink)
        self.assertEqual(False, can_buy)

    def test_food_reducing_drunkenness(self):
        self.pub.sell_customer_drink(self.customer, self.drink)
        self.pub.sell_customer_food(self.customer, self.food)
        self.assertEqual(1, self.customer.drunkenness)

    def test_drinks_list_length(self):
        self.pub.drinks_list.append(self.drink)
        self.pub.drinks_list.append(self.drink_2)
        list_len = len(self.pub.drinks_list)
        self.assertEqual(2, list_len)

    def test_stock_value(self):
        self.pub.drinks_list.append(self.drink)
        self.pub.drinks_list.append(self.drink_2)
        self.pub.incease_stock_value(self.pub.drinks_list)
        total = self.pub.stock_value
        self.assertEqual(12, total)
        
        

    

    
