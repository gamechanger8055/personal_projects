from datetime import datetime,timedelta
#import timedelta
from src.services.calendar import EventCalendar

def main():
    calendar = EventCalendar()

    user_a = calendar.create_user("A", datetime.strptime("10:00 AM", "%I:%M %p"),
                                  datetime.strptime("07:00 PM", "%I:%M %p"))
    user_b = calendar.create_user("B", datetime.strptime("09:30 AM", "%I:%M %p"),
                                  datetime.strptime("05:30 PM", "%I:%M %p"))
    user_c = calendar.create_user("C", datetime.strptime("11:30 AM", "%I:%M %p"),
                                  datetime.strptime("06:30 PM", "%I:%M %p"))
    user_d = calendar.create_user("D", datetime.strptime("10:00 AM", "%I:%M %p"),
                                  datetime.strptime("06:00 PM", "%I:%M %p"))
    user_e = calendar.create_user("E", datetime.strptime("11:00 AM", "%I:%M %p"),
                                  datetime.strptime("07:30 PM", "%I:%M %p"))
    user_f = calendar.create_user("F", datetime.strptime("11:00 AM", "%I:%M %p"),
                                  datetime.strptime("06:30 PM", "%I:%M %p"))

    print("1st",calendar.get_users())

    team_t1 = calendar.create_team("T1", [user_c, user_e])
    team_t2 = calendar.create_team("T2", [user_b, user_d, user_f])

    calendar.create_event("Event1", datetime.now() + timedelta(days=1, hours=14),
                          datetime.now() + timedelta(days=1, hours=15),
                          [user_a, team_t1], 2)

    calendar.create_event("Event2", datetime.now() + timedelta(days=1, hours=14),
                          datetime.now() + timedelta(days=1, hours=15),
                          [user_c], 1)  # Should fail since user C is already part of Event1

    calendar.create_event("Event3", datetime.now() + timedelta(hours=15), datetime.now() + timedelta(hours=16),
                          [team_t1, team_t2], 2)

    calendar.create_event("Event4", datetime.now() + timedelta(hours=15), datetime.now() + timedelta(hours=16),
                          [user_a, team_t2], 1)

    calendar.create_event("Event5", datetime.now() + timedelta(hours=10), datetime.now() + timedelta(hours=11),
                          [user_a, user_f], 1)  # Should fail since it's outside F's working hours

    # Get Events for a time range
    user_a_events = calendar.get_events_for_user(user_a, datetime.now(), datetime.now() + timedelta(days=1))
    print("User A's Events:")
    for event in user_a_events:
        print(event.name)

    user_b_events = calendar.get_events_for_user(user_b, datetime.now(), datetime.now() + timedelta(days=1))
    print("\nUser B's Events:")
    for event in user_b_events:
        print(event.name)

    # Get Available Time Slots
    available_slots = calendar.get_available_time_slots([user_a, team_t1], 1, datetime.now())
    print("\nAvailable Time Slots for User A and Team T1:")
    for slot in available_slots:
        print(f"{slot[0]} - {slot[1]}")