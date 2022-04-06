

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
        pos = int(input("Where would you like to place?"))

        env.place(pos)

