class Cashdispenser:
    def __init__(self,account,amount):
        self.account = account
        self.amount = amount

    def get_dispensed_amount(self):
        return self.amount
