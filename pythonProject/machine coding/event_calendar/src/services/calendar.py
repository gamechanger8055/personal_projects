from src.models.user import User
import datetime


class EventCalendar:
    def __init__(self):
        self.users={}

    def create_user(self, name, start,end):
        user=User(name,start,end)
        self.users[name]=user
        return user

    def get_users(self):
        return self.users



