class User:
    def __init__(self,name,gender, phone, pincode):
        self.name = name
        self.gender = gender
        self.number = phone
        self.pincode = pincode
        self.logged_in=False
        self.orders=[]

    def login(self):
        self.logged_in=True

    def logout(self):
        self.logged_in=False

    def validate_gender(self,gender):
        return gender in ['M','F']

    def add_to_order_history(self,orders):
        self.orders.append(orders)


