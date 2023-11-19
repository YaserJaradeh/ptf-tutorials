from typing import List

SYMBOL = 'Q'
NUMBER_OF_THINGS = 8

EMPTY_SPACE = '.'


def draw_board(board: List[int]):
    for i in range(NUMBER_OF_THINGS):
        for j in range(NUMBER_OF_THINGS):
            if board[i] == j:
                print(SYMBOL, end=' ')
            else:
                print(EMPTY_SPACE, end=' ')
        print()


if __name__ == '__main__':
    board = [5, 7, 2, 0, 4, 3, 6, 1]
    draw_board(board)
