from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def add_obervers(self,observer):
        pass
    def remove_observers(self,observer):
        pass

    def notify_observers(self):
        pass

    def update_observers(self):
        pass