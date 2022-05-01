import argparse
import time
from src.environment import Environment
from src.player import Player
from src.api import Api

def main(player1, player2, shape, score, game_key = None):
    p1 = Player('X', player1)

    # If we have a game key then atleast one player should take actions through the API so it has to be a bot.
    p2 = Player('O', True, True) if game_key is not None else Player('O', player2)
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
    try:
        print(env.winner.team)
    except Exception:
        print("Tie")
    print(env.grid)

def api(game_key: str):
    api = Api(game_key)
    # api.create_game('1315')
    # api.make_move(2, 2)
    # move = api.get_opponent_move()
    # print(move)
    # print(api.get_moves())

    # outline for waiting for opponent to move:
    while True:
        opponent_move = api.get_opponent_move()
        if opponent_move:
            break
        
        print('waiting for opponent move...')
        # sleep for 2 seconds to slow down api calls
        time.sleep(2)
    
    print('got opponent move: ', opponent_move)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process inputs for tic-tac-toe')
    parser.set_defaults(p1=False)
    parser.set_defaults(p2=False)
    parser.add_argument('-p1', '--player_1', action='store_true', dest='p1')
    parser.add_argument('-p2', '--player_2', action='store_true',dest='p2')
    parser.add_argument('-shape', '--shape', type=int, dest='shape', default=3)
    parser.add_argument('-s', '--score', type=int, dest='score', default=3)
    parser.add_argument('-key', '--k', type=str, dest="game_key", default=None)

    args = parser.parse_args()
    shape = args.shape
    score = args.score
    game_key = args.game_key
    main(args.p1, args.p2, shape, score, game_key)
    # api(game_key)

