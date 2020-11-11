# Defining the class for the customer object. 

class Customer:
    #constructor
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age 
        self.drunkenness = 0

    # Method for paying for either food or drink.
    def pay_bill(self, amount):
        self.wallet -= amount

    # Method for increasing drunkenness by the drinks alchohol level.
    def increase_drunkenness(self, amount):
        self.drunkenness += amount

    # Method for decreasing drunkenness by the foods rejuvonation level. 
    def decrease_drunkenness(self, amount):
        self.drunkenness -= amount 


    