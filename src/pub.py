# Defining a class for a pub object

class Pub:
    #constructor
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.max_drunk_level = 4


    def increase_till(self, amount):
        self.till += amount

    def check_age(self, customer):
        if customer.age >= 18:
            return True 
        else:
            return False 

    def check_if_cust_is_drunk(self, customer):
        if customer.drunkenness >= self.max_drunk_level:
            return True
        else:
            return False

# A Customer should be able to buy a Drink from the Pub, reducing the money in its wallet and increasing the money in the Pub's till
    def sell_customer_drink(self, customer, drink):
        if self.check_age(customer) == True and \
           self.check_if_cust_is_drunk(customer) == False:
            drink_price = drink.price
            self.increase_till(drink_price)
            customer.pay_bill(drink_price)
            customer.increase_drunkenness(drink.alchohol_lvl)
        else:
            return False 
    
    def sell_customer_food(self, customer, food):
        self.increase_till(food.price)
        customer.pay_bill(food.price)
        customer.decrease_drunkenness(food.rejuvination_lvl)
