from enum import Enum


class BoardDisplayType(Enum):
    PUBLIC, PRIVATE = 1, 2


class Board:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.display_type = BoardDisplayType.PUBLIC
        self.members = {}  # user class
        self.lists = {}  # list class

    def update_name(self, name):
        self.name = name

    def updateDisplayType(self, display_type):
        if display_type == BoardDisplayType.PUBLIC or display_type == BoardDisplayType.PRIVATE:
            self.display_type = display_type

    def add_member(self, id, user):
        self.members[id] = user

    def remove_member(self, id):
        del self.members[id]

    def count_members(self):
        return len(self.members)

    def add_list(self, id, lists):
        self.list[id] = lists

    def remove_list(self):
        del self.list[id]

    def display_list(self):
        return self.lists

    def display_list_single(self,id):
        return self.lists[id]
