import numpy as np
from tqdm import tqdm

global visited
visited = {}



def find_best(board, max_depth=5):
    global visited
    visited = {}
    best_eval = float("-inf")
    valid = board.legal_moves
    max_depth = min(max_depth, len(valid))

    best_move = valid[-1]

    for move in valid:
        result = minimax(board.move(move), False, board.turn, 1, max_depth, float('-inf'), float('inf'))

        if result > best_eval:
            best_eval = result
            best_move = move
    print(best_eval, best_move)
    return best_move

def get_h(move, moves):
    last_enemy = moves[-1]
    last_self = moves[-2]

    e_h = np.sqrt(max(abs(move[0]-last_enemy[0]), abs(move[1]-last_enemy[1])))
    s_h = np.sqrt(max(abs(move[0]-last_self[0]), abs(move[1]-last_self[1])))

    return 0

def minimax(board, maximise, origional_player, depth, max_depth, alpha, beta):
    global visited

    # if hash(board) in visited and visited[hash(board)] <= -1/depth:
    #     return visited[hash(board)]

    if board.is_terminal or board.is_draw or max_depth == depth:
        r = board._eval(origional_player)
        visited[hash(board)] = r
        return r

    valid = board.legal_moves.copy()

    if maximise:
        best_score = float('-inf')
        for move in valid:
            updated = board.move(move)
            result = minimax(updated, False, origional_player, depth + 1, max_depth, alpha, beta)
            result += get_h(move, updated.moves)

            best_score = max(result, best_score)
            visited[hash(board)] = best_score

            if best_score >= beta:
                return best_score

            alpha = max(alpha, best_score)


        return best_score
    else:
        worst_score = float('inf')
        for move in valid:
            updated = board.move(move)
            result = minimax(updated, False, origional_player, depth + 1, max_depth, alpha, beta)
            result += get_h(move, updated.moves)

            worst_score = min(result, worst_score)
            visited[hash(board)] = worst_score

            if worst_score <= alpha:
                return worst_score

            beta = min(beta, worst_score)

        return worst_score


