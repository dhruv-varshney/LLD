class Account:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def getaccountNumber(self):
        return self.account_number
    def getbalance(self):
        return self.balance
    def deduct_balance(self,amount):
        self.balance -= amount
    def add_balance(self,amount):
        self.balance += amount
    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"





