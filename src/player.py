import random

class Player:
    def __init__(self, shape='X', human = False, online = False):
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

        return env.place(pos[1],pos[0])
    
    def bot(self, env):
        pos = random.sample(env.valid_moves,1)[0]
        pos = pos.split(',')
        for i, val in enumerate(pos):
            pos[i] = int(val)

        return env.place(pos[1],pos[0])

