class Board:
    def __init__(self,snake,ladders):
        self.snakes=snake
        self.ladders=ladders
    #
    # def add_players(self,player):
    #     self.players.append(player)
    #
    # def add_snake(self,snake):
    #     self.snakes.append(snake)
    #
    # def add_ladder(self,ladder):
    #     self.ladders.append(ladder)

    def get_final_position(self,position):
        if position in self.ladders:
            ladder=self.ladders[position]
            position=ladder.move_to_end()
        if position in self.snakes:
            snake=self.snakes[position]
            position=snake.move_to_end()
        return position

