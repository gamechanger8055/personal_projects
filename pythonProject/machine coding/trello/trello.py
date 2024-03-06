from board import Board
from user import User
class Trello:
    def __init__(self):
        self.board={}
        self.member={}

    def add_board(self,id):
        if id in self.board:
            print("Board exists in system")
        self.board[id]=Board(id)

    def remove_board(self, id):
        del self.board[id]

    def display_board(self):
        return self.board

    def display_board_single(self,id):
        return self.board[id]

    def add_member(self,id):
        if id in self.member:
            print("Member exists in system")
        self.member[id]=User(id)

    def remove_member(self, id):
        del self.member[id]

    def display_member(self):
        return self.member

import threading

class SeatBookingSystem:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.lock = threading.Lock()

    def book_seat(self, user_id, num_seats):
        with self.lock:
            if self.available_seats >= num_seats:
                print(f"User {user_id} booked {num_seats} seat(s).")
                self.available_seats -= num_seats
                return True
            else:
                print(f"User {user_id} could not book {num_seats} seat(s).")
                return False

def user_thread(user_id, num_seats, booking_system):
    if booking_system.book_seat(user_id, num_seats):
        print(f"User {user_id} successfully booked {num_seats} seat(s).")
    else:
        print(f"User {user_id} failed to book {num_seats} seat(s).")

if __name__ == "__main__":
    total_seats = 10
    booking_system = SeatBookingSystem(total_seats)

    num_users = 5
    users = []

    for i in range(num_users):
        user = threading.Thread(target=user_thread, args=(i+1, 2, booking_system))
        users.append(user)
        user.start()

    for user in users:
        user.join()

    print("All users have completed booking attempts.")
    print(f"Remaining available seats: {booking_system.available_seats}")
