from src.alg import find_best


class Actor:
    def __init__(self, icon, bot = False):
        self.icon = icon
        self.bot = bot

    def get_move(self, board):
        if self.bot:
            return find_best(board)

        board.print()
        valid_moves = board.legal_moves
        print(valid_moves)
        move_idx = int(input("Enser a key for a move: "))
        return valid_moves[move_idx]