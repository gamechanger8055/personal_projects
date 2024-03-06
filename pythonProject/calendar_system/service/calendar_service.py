
class CalendarManager:
    def __init__(self):
        self.calendar={}

    def create_calender(self,email):
        self.calendar[email]=[]

    def change_guest_response(self, function, event):
        for user in event.guest_list:


    def add_event(self,email,event):
        if email in self.calendar:
            self.calendar[email].append(event)
        else:
            self.calendar[email]=[event]
        self.add_events_in_guest_list(event)
        # for user in event.guest_list:
        #     if user not in self.calendar:
        #         self.add_event(user,event)
        notify_event(event)

    def update_event(self,email,event):
        if email in self.calendar:
            self.calendar[email].append(event)
        else:
            print("that email doesnt exist")

    def






