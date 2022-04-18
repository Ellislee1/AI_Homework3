import numpy as np

def find_best(board, max_depth=8):
    best_eval = float("-inf")
    valid = board.legal_moves

    mid_point = int(np.floor(len(board.board)/2))
    if board.board[mid_point, mid_point] == 0:
        return [mid_point, mid_point]

    best_move = valid[-1]

    for move in valid:
        print(move)
        result = minimax(board.move(move), False, board.turn, max_depth)

        if result > best_eval:
            best_eval = result
            best_move = move
    return best_move

def minimax(board, maximise, origional_player, max_depth):
    if board.is_terminal or board.is_draw or max_depth == 0:
        return board._eval(origional_player)

    valid = board.legal_moves.copy()

    if maximise:
        best_score = float('-inf')
        for move in valid:
            result = minimax(board.move(move), False, origional_player, max_depth-1)

            best_score = max(result, best_score)
        
        return best_score
    else:
        worst_score = float('inf')
        for move in valid:
            result = minimax(board.move(move), True, origional_player, max_depth-1)

            worst_score = min(result, worst_score)
        
        return worst_score

