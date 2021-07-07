import stock
import transaction

class Market:
    def __init__(self):
        self.stocks = {}
        #temp stuff for testing
        stk1 = stock.Stock(50, 0, "A")
        stk2 = stock.Stock(70, 0, "B")
        self.addStock(stk1)
        self.addStock(stk2)

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