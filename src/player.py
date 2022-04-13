

class Player:
    def __init__(self, shape='X', human = False):
        self.team = shape
        self.human = human
    
    def turn(self, env):
        if self.human:
            return self.humanTurn(env)
    
    def humanTurn(self, env):
        state = env.getState()['grid']
        print(f'The state is:\n {state}')
        pos = input("Where would you like to place?").split(',')
        for i, val in enumerate(pos):
            pos[i] = int(val)

        env.place(pos[1],pos[0])

