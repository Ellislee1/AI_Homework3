import random
import numpy as np


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

        return env.place(pos[1],pos[0])
    
    def bot(self, env):
        pos = random.sample(env.valid_moves,1)[0]
        pos = pos.split(',')
        for i, val in enumerate(pos):
            pos[i] = int(val)

        return env.place(pos[1],pos[0])

    def smartBot(self, env):
        self.generateTree(env,SearchTreeNode(env.getState()))


    def generateTree(self, env, root):
        tracker = root

        if env.findValidMoves(tracker.grid).size() == 0:
            if self.winner == self.turn:
                root.setUtility(1)
            else:
                root.setUtility(-1)
        else:
            root.setUtility(0)

        for move in env.findValidMoves(tracker.grid):
            env.fakePlace(env.getState()['grid'], move[0],move[1])
            newNode = SearchTreeNode(env.getState())
            tracker.children.append(newNode)
            self.generateTree(newNode)


class SearchTreeNode:
    def __init__(self, grid):
        self.grid = grid
        self.utility = 0
        self.children = []


    def setUtility(self, utility):
        self.utility = utility




        






    



