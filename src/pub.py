# Defining a class for a pub object

class Pub:
    #constructor
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.max_drunk_level = 4
        self.stock_value = 0
        self.drinks_list = []

    # Method for putting money in the till.
    def increase_till(self, amount):
        self.till += amount

    # Method that checks if a given customer is over 18.
    def check_age(self, customer):
        if customer.age >= 18:
            return True 
        else:
            return False 

    # Method that checks is a customer is too drunk to serve.
    def check_if_cust_is_drunk(self, customer):
        if customer.drunkenness >= self.max_drunk_level:
            return True
        else:
            return False

    # Method that returns the length of the drinks menu
    def drinks_menu_length(self):
        return len(self.drinks_list)
    
    # Method that increases the stock value when given the stock list.
    def incease_stock_value(self, drink_list):
        for drink in drink_list:
            self.stock_value += drink.price

    # Method for selling a customer a drink.
    def sell_customer_drink(self, customer, drink):
        if self.check_age(customer) == True and \
           self.check_if_cust_is_drunk(customer) == False:
            drink_price = drink.price
            self.increase_till(drink_price)
            customer.pay_bill(drink_price)
            customer.increase_drunkenness(drink.alchohol_lvl)
        else:
            return False 
    
    # Method that sells a customer food.
    def sell_customer_food(self, customer, food):
        self.increase_till(food.price)
        customer.pay_bill(food.price)
        customer.decrease_drunkenness(food.rejuvination_lvl)
