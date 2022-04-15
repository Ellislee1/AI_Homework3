import argparse
from src.environment import Environment
from src.player import Player
from src.api import Api

def main(player1, player2, shape, score):
    p1 = Player('X', player1)
    p2 = Player('O', player2)

    env = Environment(p1,p2, shape, to_win=score)
    env.play()
    # print(env.getState())

def parseShape(string):
    temp_string = string.replace('(','').replace(')','').replace(' ','').split(',')

    return(int(temp_string[0]),int(temp_string[1]))

def api():
    api = Api()
    # api.create_game('1315')
    # api.make_move(3, 3)
    print(api.get_moves())

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
    # api()

