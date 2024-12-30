from atm_management import AtmManagement
from cashdispenser import Cashdispenser
from transaction import Transaction


class ATMcontroller:
    def __init__(self, account_manager, card_to_account_map, card_to_user_map):
        self.account_manager = account_manager
        self.card_to_account_map = card_to_account_map
        self.card_to_user_map = card_to_user_map

    def process_card(self, card, transaction_type, amount):
        card_user = card.get_user_name(self.card_to_user_map)
        atm = AtmManagement(card, self.card_to_account_map)
        if atm.authenticate() and card_user:
            account_number = atm.get_account_number_from_card()
            account = self.account_manager.get_account(account_number)
            if account:
                print(f"Balance in Bank is {account.get_balance()}")
            else:
                print("Issue in fetching bank details. Please contact your bank")
                return
            transaction = Transaction(account, transaction_type, amount)
            transaction_id = transaction.process()
            if transaction_type == "WITHDRAW":
                cash_dispenser = Cashdispenser(account, amount)
                cash_dispensed = cash_dispenser.get_dispensed_amount()
                print(f"Cash dispensed is {cash_dispensed}")
            print(
                f"Transaction which is {transaction_type} is successfully completed. Transaction id: {transaction_id}")
            print(
                f"Final Balance for cardHolder: {card_user} with accountNumber: {account.get_account_number()} is {account.get_balance()}")
            for account_number, account in self.account_manager.get_all_accounts().items():
                print(account)
        else:
            print("There is a issue in processing the Card.")
        print("=========================================================")
