import numpy as np
from tqdm import tqdm

global visited
visited = {}

def find_best(board, max_depth=8):
    global visited
    visited = {}
    best_eval = float("-inf")
    valid = board.legal_moves

    if np.sum(board.board) == 0:
        idx = np.random.randint(len(valid))
        return valid[idx]

    best_move = valid[-1]

    for move in valid:
        result = minimax(board.move(move), False, board.turn, 1, max_depth,-2,2)

        if result > best_eval:
            best_eval = result
            best_move = move
    return best_move

def minimax(board, maximise, origional_player, depth, max_depth, alpha, beta):
    global visited
    key = hash(np.array2string(board.board))
    
    if key in visited and (visited[key] <= (-1/depth) or visited[key] >= (1/depth)):
        return visited[key]

    if board.is_terminal or board.is_draw or max_depth == depth:
        return board._eval(origional_player)/depth

    valid = board.legal_moves.copy()

    if maximise:
        best_score = float('-inf')
        for move in valid:
            result = minimax(board.move(move), False, origional_player, depth + 1, max_depth, alpha, beta)

            best_score = max(result, best_score)

            if best_score >= beta:
                visited[key] = best_score
                return best_score
            
            alpha = max(alpha, best_score)
        visited[key] = best_score
        return best_score
    else:
        worst_score = float('inf')
        for move in valid:
            result = minimax(board.move(move), True, origional_player, depth+1, max_depth, alpha, beta)

            worst_score = min(result, worst_score)

            if worst_score <= alpha:
                visited[key] = worst_score
                return worst_score
            
            beta = min(alpha, worst_score)
        visited[key] = worst_score
        return worst_score

