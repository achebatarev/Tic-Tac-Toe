from board import Board


def main():
    board = Board()

    while(True):
        while(True):
            m, n = map(int, input(
                'Enter the position of x(row, column): ').split())
            if (board.change(m, n, 'x')):
                break
            else:
                print('Wrong input')
        print(board)
        if board.win('x'):
            print('The x has won')
            break
        if board.fill_check():
            print('We have a tie here')
            break
        while(True):
            m, n = map(int, input(
                'Enter the position of o(row, column): ').split())
            if (board.change(m, n, 'o')):
                break
            else:
                print('Wrong input')
        print(board)
        if board.win('o'):
            print('The o has won')
            break
        if board.fill_check():
            print('We have a tie here')
            break


if __name__ == '__main__':
    main()
