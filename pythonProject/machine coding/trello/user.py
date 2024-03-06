class User:
    def __init__(self, id):
        self.id=id
        self.name=None
        self.email= None
        self.designation=None

    def update_name(self, name):
        self.name=name

    def update_email(self, email):
        self.email=email

    def update_designation(self,designation):
        self.designation=designation