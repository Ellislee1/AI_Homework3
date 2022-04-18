import numpy as np
import numba as nb
import copy

class Environment:
    def __init__(self, player1, player2, grid_shape = 3, to_win = 3):
        self.grid = np.zeros((grid_shape,grid_shape))
        self.to_win = to_win

        self.players = [player1, player2]
        self.valid_moves = set()

        self.turn = None

        self.genValid()

        self.winner = None

    def genValid(self):
        self.valid_moves = set()

        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i,j] == 0:
                    self.valid_moves.add(f'{j},{i}')
        
        self.valid_moves = sorted(self.valid_moves)
    
    def place(self, x,y, player):
        self.turn = player
        try:
            self.valid_moves.remove(f'{y},{x}')
        except:
            print('here',x,y)
            return False

        if player == self.players[0]:
            key = 1
        else:
            key = 2
        self.grid[x,y] = key 

        print(x,y)
        over, condition = self.checkOver([x,y], key)
        if over:
            if condition == 2:
                self.winner = 'Tie'
            else:
                self.winner = player
        
        return True

    def placeCopy(self, x, y, player):
        env_copy = copy.deepcopy(self)

        env_copy.place(x, y, player)

        return env_copy


    
    def checkOver(self, last_pos, key):
        """
        Check that the game is finished after each players move (check win condition of a player)
        """

        x,y = last_pos[0],last_pos[1]

        # Check horizontal
        if checkLongest(self.grid[:,x].flatten(), key, self.to_win):
            return True, 1
        # Check Verticle
        if checkLongest(self.grid[y,:].flatten(), key, self.to_win):
            return True, 1
        # Check main diagonal
        if checkLongest(np.diagonal(self.grid.copy(), offset = x-y), key, self.to_win):
            return True, 1
        # Check inverse diagonal
        if checkLongest(np.diagonal(np.rot90(self.grid.copy()), offset = -self.grid.shape[1]+(x+y)+1), key, self.to_win):
            return True, 1
        # check plays remaining

        if len(self.valid_moves) <= 0:
            return True, 2


        return False, 0

    def getState(self):
        state = {'grid': self.grid}
        return state

    def __hash__(self):
        s = ""
        for i in self.grid:
            for j in i:
                s += f'{j}'
            s+='|'
        return hash(s)

def checkLongest(array, k, goal):
    cur_len = 0
    longest = 0

    for i in array:
        if i == k:
            cur_len += 1
        else:
            cur_len = 0
        
        longest = max(longest,cur_len)
    return longest >= goal