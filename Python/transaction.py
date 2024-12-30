import threading
import uuid
from enum import Enum


class TransactionType(Enum):
    WITHDRAW = 1
    DEPOSIT = 2
    TRANSFER = 3


class Transaction:
    def __init__(self, account, transaction_type, amount, target_account=None):
        self.account = account
        self.type = transaction_type
        self.amount = amount
        self.lock = threading.Lock()
        self.target = target_account

    def process(self):
        with self.lock:
            if self.type.upper() == TransactionType.WITHDRAW.name:
                self.__withdraw(self.amount)
            elif self.type.upper() == TransactionType.DEPOSIT.name:
                self.__deposit(self.amount)
            elif self.type.upper() == TransactionType.TRANSFER.name:
                self.__transfer(self.amount, self.target)
            else:
                print(f"This type does Not exist")
                return
        transactionid = self.__generateTransactionId(self.type)
        return transactionid

    def __withdraw(self, amount):
        if self.account.get_balance() >= amount:
            self.account.deduct_balance(amount)
        else:
            print("Entered amount is more than the Balance in account")
            return

    def __deposit(self, amount):
        self.account.add_balance(amount)

    def __transfer(self, amount, target_account):
        if self.account.get_balance() >= amount:
            self.account.deduct_balance(amount)
            target_account.add_balance(amount)
        else:
            print("Entered amount is more than the Balance in account")
            return

    def __generateTransactionId(self, type):
        return f"TXN{type}{uuid.uuid4()}"
