import numpy as np

def findBest(env, player, depth=8):
    best_score = -np.inf
    best_move = None

    for move in env.valid_moves:
        move = parseMove(move)
        next_player = getNextPlayer(player, env)
        score = minimax(env.placeCopy(move[0], move[1], player), next_player, True, 0, player, depth)

        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move


def minimax(env, player, maximse, depth, origional_player, max_depth):
    if env.winner is not None:
        if env.winner == origional_player:
            return 1/depth
        elif env.winner == 'Tie':
            return 0
        else:
            return -1
    elif depth == max_depth:
        return 0

    if maximse:
        best_score = -np.inf
        for move in env.valid_moves:
            move = parseMove(move)
            next_player = getNextPlayer(player, env)
            score = minimax(env.placeCopy(move[0], move[1], player), next_player, True, depth+1, origional_player, max_depth)

            best_score = max(best_score, score)
        return best_score
    else:
        worst_score = np.inf

        for move in env.valid_moves:
            move = parseMove(move)
            next_player = getNextPlayer(player, env)
            score = minimax(env.placeCopy(move[0], move[1], player), next_player, True, depth+1, origional_player, max_depth)

            worst_score = min(worst_score, score)
        return worst_score

def parseMove(move):
    return [int(i) for i in move.split(',')]

def getNextPlayer(player, env):
    return env.players[0] if player != env.players[0] else env.players[1]