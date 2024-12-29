class AtmManagement:
    def __init__(self,card,card_to_account_map):
        self.card = card
        self.card_to_account_map = card_to_account_map
    def authenticate(self):
        print(f"Card Authenticated successfully")
        return True
    def get_account_number_from_card(self):
        return self.card_to_account_map[self.card.get_card_number()]
