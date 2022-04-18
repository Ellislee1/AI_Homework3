from src.environment import Environment
from src.player import Player
import numpy as np

def minimax(env, origional_player, maximising, max_depth = 8):
    if env.winner is not None:
        if env.winner == origional_player:
            return 1
        elif env.winner == 'Tie':
            return 0
        else:
            return -1
    elif max_depth == 0:
        return 0

    if maximising:
        best_eval = -np.inf

        for move in  env.valid_moves:
            result = minimax(env.copyMove(move), False, origional_player, max_depth -1)
            best_eval = max(best_eval, result)
        return best_eval
    else:
        worst_eval = np.inf
        for move in  env.valid_moves:
            result = minimax(env.copyMove(move), False, origional_player, max_depth -1)
            worst_eval = min(result,worst_eval)
        return worst_eval
    

        

def findBestMove(env, max_depth = 8):
    best_eval = -np.inf
    best_move = None
    move = None
    for move in env.valid_moves:
        pos = move.split(',')
        pos = [int(i) for i in pos]
        result = minimax(env.copyMove(move), env.turn, False, max_depth)
        if result > best_eval:
            best_eval = result
            best_move = move
    print(best_move)
    
    return best_move