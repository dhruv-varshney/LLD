from Card import Card
from account import Account
from accountManager import AccountManager
from atmcontoller import ATMcontroller


class ATMDemo:
    @staticmethod
    def run():
        card_to_user_map = {"6522-6000-1086-4380": "Dhruv", "6522-6000-1086-4382": "Harsh",
                            "6522-6000-1086-4383": "Ashish"}
        # card1.get_user_name(card_to_user_map)
        card_to_account_map = {"6522-6000-1086-4380": "1234", "6522-6000-1086-4382": "4567",
                               "6522-6000-1086-4381": "8901", "6522-6000-1086-4383": "1024"}
        account1 = Account("1234", 500000)
        account2 = Account("4567", 80000)
        account3 = Account("8902", 30000)
        account4 = Account("67890", 50000)
        account5 = Account("23459", 500000)
        account_manager = AccountManager()
        account_manager.add(account1)
        account_manager.add(account2)
        account_manager.add(account3)
        account_manager.add(account4)
        account_manager.add(account5)
        atmcontroller = ATMcontroller(account_manager, card_to_account_map, card_to_user_map)
        card1 = Card("6522-6000-1086-4380", 1970)
        atmcontroller.process_card(card1, "WITHDRAW", 40000)
        card2 = Card("6522-6000-1086-4382", 1972)
        atmcontroller.process_card(card2, "DEPOSIT", 20000)
        card3 = Card("6522-6000-1086-4381", 1973)
        atmcontroller.process_card(card3, "WITHDRAW", 40000)
        card4 = Card("6522-6000-1086-4383", 1974)
        atmcontroller.process_card(card4, "WITHDRAW", 40000)
        card5= Card("6522-6000-1086-4380",1970)
        atmcontroller.process_card(card5,"TRANSFER",4000, "0000")
        card6= Card("6522-6000-1086-4380",1970)
        atmcontroller.process_card(card6,"TRANSFER",4000, "4567")



if __name__ == "__main__":
    ATMDemo.run()
