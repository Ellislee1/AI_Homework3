import random
from src.minimax import findBest

class Player:
    def __init__(self, shape='X', human = False):
        self.team = shape
        self.human = human
    
    def turn(self, env):
        if self.human:
            return self.humanTurn(env)
        if self.bot:
            return self.bot(env)
    
    def humanTurn(self, env):
        print(f'Valid moves are : {env.valid_moves}')
        state = env.getState()['grid']
        print(f'The state is:\n {state}')
        pos = input("Where would you like to place?").split(',')
        for i, val in enumerate(pos):
            pos[i] = int(val)

        return env.place(pos[1],pos[0], self)
    
    def bot(self, env):
        best_move = findBest(env, self)

        if best_move is None:
            return env
        pos = best_move

        print(pos)
        return env.place(pos[1],pos[0], self)

