import numpy as np

class Board:
    def __init__(self, board, turn, players, win_score):
        self.board = board
        self.turn = turn
        self.players = players
        self.win_score = win_score

        self.condition = {
            1: lambda x,y,k: self.check_requirement(self.board[:,x].flatten(), k, self.win_score),
            2: lambda x,y,k: self.check_requirement(self.board[y,:].flatten(), k, self.win_score),
            3: lambda x,y,k: self.check_requirement(np.diagonal(self.board.copy(), offset = x-y), k, self.win_score),
            4: lambda x,y,k: self.check_requirement(np.diagonal(np.rot90(self.board.copy()), offset = -self.board.shape[1]+(x+y)+1), k, self.win_score)
        }
    
    def move(self, placement):
        # Placement form is [y,x]
        # Numpy form is [y,x]
        y,x = placement[0], placement[1]
        next_player = self.players[0] if self.turn != self.players[0] else self.players[1]
        board = self.board.copy()
        board[y,x] = self.turn.icon

        return Board(board, next_player, self.players, self.win_score)
    
    @property
    def is_terminal(self):
        p = self.players[0] if self.turn == self.players[1] else self.players[1]

        for y in range(self.board.shape[0]):
            for x in range(self.board.shape[1]):
                for _, c in self.condition.items():
                    if c(x,y,p.icon):
                        return True
                
        return False

    @property
    def is_draw(self):
        return (not self.is_terminal) and (len(self.legal_moves) == 0)

    @property 
    def legal_moves(self):
        valid = []

        for y in range(self.board.shape[0]):
            for x in range(self.board.shape[1]): 
                if self.board[y,x] == 0:
                    valid.append([y,x])
        
        return np.array(valid)
    
    def print(self):
        print('\n')
        for y in self.board:
            print(y)
        print('\n')


    def check_requirement(self, array, k, l):
        max_length = 0
        length = 0

        for i in array:
            if i == k:
                length += 1
            else:
                length = 0
            
            max_length = max(max_length, length)

            if max_length >= l:
                return True
        
        return max_length >= l

    def _eval(self, player):
        if self.is_terminal and self.turn != player:
            return 1
        if self.is_terminal and self.turn == player:
            return -1
        
        return 0




class Player:
    def __init__(self, icon):
        self.icon = icon
