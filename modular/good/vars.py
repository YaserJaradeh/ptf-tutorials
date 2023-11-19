from typing import List


def draw_board(
        board: List[int],
        symbol: str = 'Q',
        number_of_things: int = 8,
        empty_space: str = '.'
):
    for i in range(number_of_things):
        for j in range(number_of_things):
            if board[i] == j:
                print(symbol, end=' ')
            else:
                print(empty_space, end=' ')
        print()


class Board:
    size: int
    board: List[int]
    symbol: str = 'Y'
    empty_space: str = '*'

    def __init__(self, size: int, symbol: str = 'Y', empty_space: str = '*'):
        self.size = size
        self.board = [0] * size
        self.symbol = symbol
        self.empty_space = empty_space

    def set_board(self, board: List[int]):
        self.board = board

    def draw(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i] == j:
                    print(self.symbol, end=' ')
                else:
                    print(self.empty_space, end=' ')
            print()


if __name__ == '__main__':
    board = [5, 7, 2, 0, 4, 3, 6, 1]
    draw_board(board)
    print("=" * 10)
    board = Board(8)
    board.set_board([5, 7, 2, 0, 4, 3, 6, 1])
    board.draw()
