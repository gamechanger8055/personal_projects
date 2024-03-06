from enums.event_state import EventState


class Events:
    def __init__(self,id,title,start,end,location,owner, guest_list):
        self.title=title
        self.start=start
        self.end=end
        self.location=location
        self.owner=owner
        self.guest_list=guest_list
        self.state=EventState.NEUTRAL

    def accept_event(self):
        self.state=EventState.ACCEPTED

    def reject_state(self):
        self.state=EventState.REJECTED

    def add_guests(self,guest):
        self.guest_list.append(guest)

    def remove_guests(self,guest):
        self.guest_list.remove(guest)