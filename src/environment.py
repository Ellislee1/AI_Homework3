import numpy as np

class Environment:
    def __init__(self, player1, player2, grid_shape = (3,3), to_win = 3):
        self.grid = np.zeros(grid_shape)
        self.to_win = to_win

        self.player_1 = player1
        self.player_2 = player2

        self.turn = np.random.choice([self.player_1,self.player_2],1)[0]

        while not(self.nextTurn()):
            pass

    def nextTurn(self):
        self.turn.turn(self)
        if self.turn == self.player_1:
            self.turn = self.player_2
            return self.checkOver(1)
        else:
            self.turn = self.player_1
            return self.checkOver(2)
    
    def place(self, position):
        if self.turn == self.player_1:
            key = 1
        else:
            key = 2

        flattened = self.grid.copy().flatten()
        flattened[position] = key
        flattened = flattened.reshape(self.grid.shape)
        self.grid = flattened

    
    def checkOver(self, key):
        if np.count_nonzero(self.grid == key) < self.to_win:
            return False
        
        for i in range(self.grid.shape[0]):
            unique, counts = np.unique(self.grid[i,:], return_counts=True)
            if key in unique[0] and counts[0] >= self.to_win:
                return True

        for i in range(self.grid.shape[1]):
            unique, counts = np.unique(self.grid[:,i], return_counts=True)
            if len(unique) == 1 and unique[0] == key and counts[0] >= self.to_win:
                return True
        
        return False

        


    def getState(self):
        state = {
            'grid': self.grid.copy(),
            'turn': self.turn
        }

        return state
