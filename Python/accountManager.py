import threading


class AccountManager:
    def __init__(self):
        self.dict = {}
        self.lock = threading.Lock()
    def add(self,account):
        with self.lock:
            self.dict[account.getaccountNumber()] = account
    def get_all_accounts(self):
        with self.lock:
            return self.dict

    def get_account(self, account_number):
        with self.lock:
            return self.dict.get(account_number)


