from src.model.board import Board
from src.model.dice import Dice
from src.model.user import User


class SnakeAndLadder:
    def __init__(self,ladders,snakes,players,start=1,end=100):
        self.board=Board(snakes,ladders)
        self.players=[]
        for player in players:
            self.players.append(User(player,self.board))


    def play(self):
        curr=0
        while(1):
            cur_player=self.players[curr]
            dic=Dice()
            dice_roll=dic.roll()
            cur_player.move(dice_roll)
            if cur_player.has_won():
                return
            curr+=1
            curr=curr%len(self.players)