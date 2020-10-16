from copy import deepcopy


class Board:
    def __init__(self, board=None):
        if board is None:
            self.board = [
                ['0', '0', '0'],
                ['0', '0', '0'],
                ['0', '0', '0']]
        else:
            self.board = board

    def change(self, row, col, side):
        if row <= 0 or row > len(self.board) or col <= 0 or col > len(self.board):
            return False
        elif self.board[row-1][col-1] in ('x', 'o'):
            return False
        self.board[row-1][col-1] = side
        return True

    def change_board(self, row, col, side):
        board_copy = deepcopy(self.board)
        if row <= 0 or row > len(self.board) or col <= 0 or col > len(self.board):
            print('Out of bounds')
            return False
        elif self.board[row-1][col-1] in ('x', 'o'):
            print('This place is taken')
            return False
        board_copy[row-1][col-1] = side
        return board_copy

    def check_horizontal(self, side):
        for row in self.board:
            match = 0
            for cell in row:
                if cell == side:
                    match += 1
            if match >= 3:
                return True
        return False

    def check_vertical(self, side):
        for n in range(len(self.board[-1])):
            match = 0
            for m in range(len(self.board)):
                if self.board[m][n] == side:
                    match += 1
            if match >= 3:
                return True
        return False

    def check_diagonal_left(self, side):
        match = 0
        m = 0
        n = 0
        while m < len(self.board):
            if self.board[m][n] == side:
                match += 1
            m += 1
            n += 1
        if match >= 3:
            return True
        return False

    def check_diagonal_right(self, side):
        match = 0
        m, n = len(self.board)-1, 0
        while m >= 0:
            if self.board[m][n] == side:
                match += 1
            m -= 1
            n += 1
        if match >= 3:
            return True
        return False

    def win(self, side):
        if self.check_horizontal(side) or self.check_vertical(side) or self.check_diagonal_left(side) or self.check_diagonal_right(side):
            return True
        return False

    def get_available_moves(self):
        moves = []
        for m, row in enumerate(self.board):
            for n, cell in enumerate(row):
                if cell == '0':
                    moves.append((m, n))
        return moves
# returns True is there is no empty space left

    def fill_check(self):
        return not any('0' in row for row in self.board)

    def __repr__(self):
        output = ''
        for row in self.board:
            output += ' '.join(row)
            output += '\n'
        return output
