import market as m
import transaction as t

class Player:
    def __init__(self, inital_balance):
        self.balance = inital_balance
        self.market = m.Market()
        self.owned = {}

    def createTransaction(self):
        self.market.displayAll()
        print("NEW TRANSACTION")
        trans_type = input("TYPE: ")
        ticker = input("TICKER: ")
        quantity = int(input("QUANTITY: "))
        confirm = input("Enter y to confirm: ")
        if confirm == "y":
            o = 0
            if ticker in self.owned.keys():
                o = self.owned[ticker]
            transact = t.Transaction(ticker, trans_type, quantity, o, self.balance)
        else:
            transact = t.Transaction.failed()
        return transact

    def act(self):
        transact = self.createTransaction()
        receipt = self.market.handleTransaction(transact)
        if receipt.trans_type == "RECEIPT":
            self.balance = receipt.balance
            self.owned[receipt.ticker] = receipt.owned
        print(receipt)
        