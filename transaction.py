class Transaction:
    def __init__(self, ticker, trans_type, quantity, owned, balance):
        self.ticker = ticker
        self.trans_type = trans_type
        self.quantity = quantity
        self.owned = owned
        self.balance = balance

    @classmethod
    def failed(cls):
        return cls("FAILED", "FAILED", 0, 0, 0)

    def __str__(self):
        s = "STK\tTYPE\tQ\tOwn\tBal\n"
        s += self.ticker + "\t"
        s += self.trans_type + "\t"
        s += str(self.quantity) + "\t"
        s += str(self.owned) + "\t"
        s += str(self.balance)
        return s

