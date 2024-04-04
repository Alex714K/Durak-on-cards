class AI:
    def __init__(self):
        self.turn = None

    def who_turn(self, turn, num):
        if num == 0:
            self.turn = turn

    def give_board(self, board):
        self.board = board
