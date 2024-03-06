from models.admin import Admin
from models.batch import Batch
from models.student import Student

from services.GenderBasedStrategy import GenderBasedStrategy
from services.HigherCapacityStrategy import HigherCapacityStrategy


class BatchController:
    def __init__(self):
        self.students = []
        self.batches = []
        self.admins = []
        self.time_map={"Morning":0,"Noon":1, "Evening":2}


    def register(self, name, gender, role):
        if role == "Student":
            student = Student(name, gender, role)
            self.students.append(student)
            print("{} registered successfully as a student".format(name))
            return student
        elif role == "Admin":
            admin = Admin(name, gender, role)
            self.admins.append(admin)
            print("{} registered successfully as an admin".format(name))
            return admin

    def createBatch(self, admin, capacity, stream, timing):
        if admin in self.admins:
            batch = Batch(admin, capacity, stream, self.time_map[timing])
            self.batches.append(batch)
            print("{} created the batch successfully with capacity of {}".format(admin.name, capacity))
            return batch
        return "Sorry the admin is not present in our system"

    def enroll(self, student, stream):
        if student in self.students:
            student.stream = stream
            print("{} enrolled successfully to {} stream".format(student.name, stream))
        else:
            print("{} cannot be enrolled to {} stream".format(student, stream))

    def allocateBatch(self, admin, student, criteria):
        if admin in self.admins and student.stream:
            eligible_batches = [batch for batch in self.batches if batch.stream == student.stream]
            if criteria=="Gender Based":
                return GenderBasedStrategy().allocate(eligible_batches,student)

            elif criteria=="Higher capacity":
                return HigherCapacityStrategy().allocate(eligible_batches,student)
        else:
            print("Please contact admin or front desk officer for further support")
