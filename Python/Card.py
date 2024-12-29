class Card:
    def __init__(self,card_number,pin):
        self.card_number = card_number
        self.pin = pin
    def get_card_number(self):
        return self.card_number
    def get_user_name(self,card_to_user_map):
        if(self.card_number in card_to_user_map):
            print(f"Welcome {card_to_user_map[self.card_number]}")
            return True
        else:
            print(f"Card is Invalid")
            return False
