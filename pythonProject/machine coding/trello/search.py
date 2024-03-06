from abc import ABC, abstractmethod

class Search(ABC):
    @abstractmethod
    def search_by_assigned_user(self,user):
        pass
    def search_by_created_at(self, time):
        pass
    def search_by_eta(self, eta):
        pass
    def search_by_priority(self, priority):
        pass

class Filter(Search):
    def __init__(self):
        self.assigned_user={}
        self.created_at={}
        self.eta={}
        self.priority={}

    def search_by_eta(self, eta):
        return self.eta.get(eta)

    def search_by_priority(self, priority):
        return self.priority.get(priority)

    def search_by_assigned_user(self, assigned_user):
        return self.eta.get(assigned_user)

    def search_by_created_at(self, created_at):
        return self.eta.get(created_at)
