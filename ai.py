from board import Board


def minmax(board, player, ai, human):
    if(board.win(human)):
        return -10
    elif(board.win(ai)):
        return 10
    elif board.fill_check():
        return 0
    else:
        values = []
        moves = board.get_available_moves()
        for m, n in moves:
            if player == human:
                values.append(
                    minmax(Board(board.change_board(m+1, n+1, player)), ai, ai, human))
            else:
                values.append(
                    minmax(Board(board.change_board(m+1, n+1, player)), human, ai, human))
        if player == human:
            return min(values)
        else:
            return max(values)


def ai_move(board):
    values = []
    human = 'x'
    ai = 'o'
    possibilities = board.get_available_moves()
    for y, x in possibilities:
        values.append(
            (minmax(Board(board.change_board(y+1, x+1, ai)), human, ai, human), (y, x)))
    y, x = max(values, key=lambda x: x[0])[1]
    board.change(y+1, x+1, ai)
