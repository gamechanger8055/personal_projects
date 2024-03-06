class Card:
    def __init__(self, card_no,expiry,cvv,holder_name, bank_name,pin, bank_account):
        self.card_no=card_no
        self.expiry=expiry
        self.cvv=cvv
        self.holder_name=holder_name
        self.bank=bank_name
        self.pin=pin
        self.account=bank_account

    def ifPinEnteredIsCorrect(self,pin):
        return pin==self.pin

