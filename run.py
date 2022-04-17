import argparse
from src.environment import Environment
from src.player import Player

def main(player1, player2, shape, score):
    p1 = Player('X', player1)
    p2 = Player('O', player2)

    env = Environment(p1,p2, shape, to_win=score)
    # print(env.getState())
    play(env)

def play(env):
    current = env.players[0]
    i=0

    while env.winner is None:
        current.turn(env)
        i = (i+1) % 2
        current= env.players[i]
    print(env.winner)
    print(env.grid)

def parseShape(string):
    temp_string = string.replace('(','').replace(')','').replace(' ','').split(',')

    return(int(temp_string[0]),int(temp_string[1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process inputs for tic-tac-toe')
    parser.set_defaults(p1=False)
    parser.set_defaults(p2=False)
    parser.add_argument('-p1', '--player_1', action='store_true', dest='p1')
    parser.add_argument('-p2', '--player_2', action='store_true',dest='p2')

    parser.add_argument('-shape', '--shape', type=int, dest='shape', default=3)
    parser.add_argument('-s', '--score', type=int, dest='score', default=3)
    args = parser.parse_args()
    shape = args.shape
    score = args.score
    main(args.p1, args.p2, shape, score)

