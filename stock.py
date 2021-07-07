import transaction
import random
import math

class Stock:
    def __init__(self, initial_price, volatility, drift, ticker):
        self.price = initial_price
        self.volatility = volatility
        self.ticker = ticker
        self.existing = True
        self.drift = drift
        self.record = [initial_price]

    def remove(self):
        self.existing = False

    def exists(self):
        return self.existing

    def validate(self, transact):
        if transact.trans_type == "BUY":
            if self.price * transact.quantity > transact.balance:
                return False
        elif transact.trans_type == "SELL":
            if transact.quantity > transact.owned:
                return False
        else:
            return False
        return True
    
    def performTransaction(self, transact):
        if transact.trans_type == "BUY":
            transact.owned += transact.quantity
            transact.trans_type = "RECEIPT"
            transact.balance -= transact.quantity * self.price
        elif transact.trans_type == "SELL":
            transact.owned -= transact.quantity
            transact.trans_type = "RECEIPT"
            transact.balance += transact.quantity * self.price
        return transact

    def update(self):
        random.seed()
        change = random.lognormvariate(self.drift, self.volatility)
        self.price = self.price*change
        self.record.append(self.price)