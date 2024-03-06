import time
from enum import Enum

class Status(Enum):
    TODO, INPROGRESS, DONE, LIVE, DEPLOYMENT=1,2,3,4,5
class Cards:
    def __init__(self,id):
        self.id=id
        self.name=None
        self.description=None
        self.assigner_user=None
        self.priority=None
        self.eta=None
        self.status=Status.TODO
        self.created_at=None
        self.finished_at=None

    def update_name(self,name):
        self.name=name

    def update_desc(self, desc):
        self.description=desc

    def assign_user(self,user):
        self.assigner_user=user

    def unassign_user(self):
        self.assigner_user=None

    def delete_user(self, id):
        del self.assigner_user[id]

    def update_priority(self, priority):
        self.priority=priority

    def created_time(self):
        self.created_at=time.Now()

    def finished_time(self, time):
        self.finished_at=time

    def eta_time(self, time):
        self.eta=time

    def update_status(self,status):
        self.status=status

