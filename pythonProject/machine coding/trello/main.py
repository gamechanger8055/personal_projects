from trello import Trello
import random


def main():
    id=random.Random()
    trello=Trello()
    trello.add_board(1)
    print(trello.display_board())
    trello.remove_board(1)
    print(trello.display_board())
    trello.add_member(1)
    print(trello.display_member())
    trello.remove_member(1)
    print(trello.display_member())

    # observer pattern and concurrency

main()