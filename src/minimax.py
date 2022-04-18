import numpy as np

global visited
visited = {}

def findBest(env, player, depth=50):
    global visited
    visited = {}
    best_score = -np.inf
    best_move = None

    for move in env.valid_moves:
        move = parseMove(move)
        next_player = getNextPlayer(player, env)
        score = minimax(env.placeCopy(move[0], move[1], player), next_player, False, 0, player, depth)

        if score > best_score:
            best_score = score
            best_move = move
    
    print(best_score, best_move)
    return best_move


def minimax(env, player, maximse, depth, origional_player, max_depth):
    global visited
    if hash(env) in visited:
        return visited[hash(env)]
        

    if env.winner is not None:
        if env.winner == origional_player:
            visited[hash(env)] = 1/(depth+1)
            return 1/(depth+1)
        elif env.winner == 'Tie':
            visited[hash(env)] = 0
            return 0
        else:
            visited[hash(env)] = -1
            return -1
    elif depth == max_depth:
        return 0

    if maximse:
        best_score = -np.inf
        for move in env.valid_moves:
            move = parseMove(move)
            next_player = getNextPlayer(player, env)
            score = minimax(env.placeCopy(move[0], move[1], player), next_player, False, depth+1, origional_player, max_depth)
            best_score = max(best_score, score)
        visited[hash(env)] = best_score
        return best_score
    else:
        worst_score = np.inf

        for move in env.valid_moves:
            move = parseMove(move)
            next_player = getNextPlayer(player, env)
            score = minimax(env.placeCopy(move[0], move[1], player), next_player, True, depth+1, origional_player, max_depth)

            worst_score = min(worst_score, score)
        visited[hash(env)] = worst_score
        return worst_score

def parseMove(move):
    return [int(i) for i in move.split(',')]

def getNextPlayer(player, env):
    return env.players[0] if player.team != env.players[0].team else env.players[1]