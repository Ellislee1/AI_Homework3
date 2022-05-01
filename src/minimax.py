import numpy as np

global visited
visited = {}



        

def findBest(env, player, depth=8):
    global visited
    visited = {}
    best_score = -np.inf
    best_move = None


    if depth is None:
        depth = len(env.valid_moves)+1
        print(depth)

    if len(env.valid_moves) == 1:
        v = env.valid_moves.pop()
        env.valid_moves = set([v])
        return parseMove(v)
    # elif f'{int(np.floor(env.grid.shape[1]/2))},{int(np.floor(env.grid.shape[1]/2))}' in env.valid_moves:
    #     return parseMove(f'{int(np.floor(env.grid.shape[1]/2))},{int(np.floor(env.grid.shape[1]/2))}')

    for move in env.valid_moves:
        
        move = parseMove(move)
        next_player = getNextPlayer(player, env)
        score = minimax(env.placeCopy(move[1], move[0], player), next_player, False, 0, player, depth, move)

        if score > best_score:
            best_score = score
            best_move = move
    
    print(best_score, best_move)
    
    return best_move


def minimax(env, player, maximse, depth, origional_player, max_depth, last_move):
    global visited

    if env.winner is not None or depth >= max_depth:
        if env.winner == 'Tie' or depth >= max_depth:
            return 0
        elif env.winner.team == origional_player.team:
            return -1
        else:
            return 1

    if maximse:
        best_score = -np.inf

        for move in env.valid_moves:
            move = parseMove(move)
            score = minimax(env.placeCopy(move[1], move[0], player), getNextPlayer(player, env), False, depth+1, origional_player, max_depth, move)

            best_score = max(best_score, score)
    else:
        best_score = np.inf
        for move in env.valid_moves:
            move = parseMove(move)
            score = minimax(env.placeCopy(move[1], move[0], player), getNextPlayer(player, env), True, depth+1, origional_player, max_depth, move)
            best_score = min(best_score, score)

    return best_score

def parseMove(move):
    return [int(i) for i in move.split(',')]

def getNextPlayer(player, env):
    return env.players[0] if player.team != env.players[0].team else env.players[1]