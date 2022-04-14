import numpy as np
from numpy.lib.twodim_base import diag
import numba as nb

class Environment:
    def __init__(self, player1, player2, grid_shape = 3, to_win = 3):
        self.grid = np.zeros((grid_shape,grid_shape))
        self.to_win = to_win

        self.player_1 = player1
        self.player_2 = player2
        self.valid_moves = set()

        self.genValid()

        self.winner = None

    def genValid(self):
        self.valid_moves = set()

        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                self.valid_moves.add(f'{j},{i}')

    def play(self, turn = None):
        self.turn = turn
        if self.turn is None:
            self.turn = np.random.choice([self.player_1,self.player_2],1)[0]

        while self.winner is None:
            self.nextTurn()
        
        if self.winner == 'Tie':
            print('Match was a Tie!')
        else:
            print(f'Player {self.winner.team} Wins!!!')
            print(self.grid)

    def nextTurn(self):
        success = False
        while not success:
            success = self.turn.turn(self)

        if self.turn == self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1
    
    def place(self, x,y):
        try:
            self.valid_moves.remove(f'{y},{x}')
        except:
            return False

        if self.turn == self.player_1:
            key = 1
        else:
            key = 2
        self.grid[x,y] = key 

        over, condition = self.checkOver([x,y], key)
        if over:
            if condition == 2:
                self.winner = 'Tie'
            else:
                self.winner = self.turn
        
        return True

    
    def checkOver(self, last_pos, key):
        """
        Check that the game is finished after each players move (check win condition of a player)
        """

        # Check horizontal
        if checkLongest(self.grid[:,last_pos[1]].flatten(), key, self.to_win):
            return True, 1
        # Check Verticle
        if checkLongest(self.grid[last_pos[0],:].flatten(), key, self.to_win):
            return True, 1
        # Check main diagonal
        if checkLongest(np.diagonal(self.grid.copy(), offset = last_pos[1]-last_pos[0]), key, self.to_win):
            return True, 1
        # Check inverse diagonal
        if checkLongest(np.diagonal(np.rot90(self.grid.copy()), offset = -self.grid.shape[1]+(last_pos[1]+last_pos[0])+1), key, self.to_win):
            return True, 1
        # check plays remaining

        if len(self.valid_moves) <= 0:
            return True, 2


        return False, 0

    def getState(self):
        state = {
            'grid': self.grid.copy(),
            'turn': self.turn
        }

        return state


@nb.njit()
def checkLongest(array: np.array, k: int, goal: int):
    cur_len = 0
    longest = 0

    for i in array:
        if i == k:
            cur_len += 1
        else:
            cur_len = 0
        
        longest = max(longest,cur_len)
    return longest >= goal