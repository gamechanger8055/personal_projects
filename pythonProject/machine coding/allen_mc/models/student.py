from models.admin import Admin


class Student(Admin):
    def __init__(self,name, gender, role):
        super().__init__(name,gender, role)
        self.stream=None