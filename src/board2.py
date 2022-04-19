import numpy as np
import numba as nb

class Board:
    def __init__(self, board, turn, players, win_score, moves = []):
        self.board = board
        self.turn = turn
        self.players = players
        self.win_score = win_score

        self.moves = moves

        self.condition = {
            1: lambda x,y,k: check_requirement(self.board[:,x].flatten(), k, self.win_score),
            2: lambda x,y,k: check_requirement(self.board[y,:].flatten(), k, self.win_score),
            3: lambda x,y,k: check_requirement(np.diagonal(self.board.copy(), offset = x-y), k, self.win_score),
            4: lambda x,y,k: check_requirement(np.diagonal(np.rot90(self.board.copy()), offset = -self.board.shape[1]+(x+y)+1), k, self.win_score)
        }
    
    def move(self, placement):
        # Placement form is [y,x]
        # Numpy form is [y,x]
        y,x = placement[0], placement[1]
        next_player = self.players[0] if self.turn != self.players[0] else self.players[1]
        board = self.board.copy()
        board[y,x] = self.turn.icon

        new_moves = self.moves.copy()
        new_moves.append(placement)

        return Board(board, next_player, self.players, self.win_score,new_moves)
    
    @property
    def is_terminal(self):
        if len(self.moves) == 0:
            return False

        y,x = self.moves[-1][0], self.moves[-1][1]
        p = self.players[0] if self.turn == self.players[1] else self.players[1]

        # for y in range(self.board.shape[0]):
        #     for x in range(self.board.shape[1]):
        for i, c in self.condition.items():
            if c(x,y,p.icon):
                return True
            
                
        return False

    @property
    def is_draw(self):
        return (not self.is_terminal) and (len(self.legal_moves) == 0)

    @property 
    def legal_moves(self):
        valid = []
        distance = []

        for y in range(self.board.shape[0]):
            for x in range(self.board.shape[1]): 
                if self.board[y,x] == 0:
                    if len(self.moves) >0:
                        d = max(abs(self.moves[-1][0]-y),abs(self.moves[-1][1]-x))
                        distance.append(d)

                    valid.append([y,x])
        

        valid = np.array(valid)
        if len(self.moves) > 0 and self.turn.bot:
            order = np.argsort(distance)[:8]
            valid = valid[order]
        return valid
    
    def print(self):
        print('\n')
        for y in self.board:
            print(y)
        print('\n')

    def _eval(self, player):
        if self.is_terminal and self.turn != player:
            return 1
        if self.is_terminal and self.turn == player:
            return -1
        
        return 0

    def count_pieces(self, player):
        return np.count_nonzero(self.board == player.icon)



@nb.njit()
def check_requirement( array, k, l):
        max_length = 0
        length = 0

        if np.count_nonzero(array == k) < l:
            return False

        for i in array:
            if i == k:
                length += 1
            else:
                length = 0
            
            max_length = max(max_length, length)

            if max_length >= l:
                return True
        
        return max_length >= l
