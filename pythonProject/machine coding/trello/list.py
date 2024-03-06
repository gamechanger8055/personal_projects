class List:
    def __init__(self, id, name):
        self.cards = {}
        self.id = id
        self.name = name

    def update_name(self, name):
        self.name = name

    def add_cards(self, id, card):
        self.cards[id] = card

    def remove_card(self,id):
        del self.cards[id]

    def move_cards(self,id1, id2):
        card1=self.cards[id1]
        self.remove_card(id1)
        self.add_cards(id2,card1)

    def display_card(self):
        return self.cards

    def display_card_single(self, id):
        return self.cards[id]



