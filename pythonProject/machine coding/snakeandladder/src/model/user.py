class User:
    def __init__(self,id,board):
        self.id=id
        self.position=-1
        self.board=board

    def has_won(self):
        return self.position==100

    def move(self, dice_roll):
        if self.position+dice_roll>100:
            print("Invalid move")
        self.position+=dice_roll
        self.position=self.board.get_final_position(self.position)




