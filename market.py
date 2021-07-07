import stock
import transaction

class Market:
    def __init__(self):
        self.stocks = {}
        #temp stuff for testing

    @classmethod
    def simple_market(cls):
        m = cls()
        stk1 = stock.Stock(50, 0.05, 0, "A")
        stk2 = stock.Stock(70, 0.1, 0.05, "B")
        m.addStock(stk1)
        m.addStock(stk2)
        return m

    def addStock(self, stk):
        if isinstance(stk, stock.Stock):
            self.stocks[stk.ticker] = stk

    def removeStock(self, ticker):
        self.stocks[ticker].remove()

    def validateTransaction(self, transact):
        if isinstance(transact, transaction.Transaction):
            if transact.ticker in self.stocks.keys() and self.stocks[transact.ticker].exists():
                return self.stocks[transact.ticker].validate(transact)
        return False

    def handleTransaction(self, transact):
        if self.validateTransaction(transact):
            return self.stocks[transact.ticker].performTransaction(transact)
        else:
            return transaction.Transaction.failed()

    def displayAll(self):
        for stk in self.stocks.values():
            print(stk.ticker + "\t" + str(stk.price))

    def update(self):
        for key in self.stocks.keys():
            self.stocks[key].update()