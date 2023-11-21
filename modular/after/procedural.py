import random
from typing import List, Tuple, Optional


class MazeGenerator:
    def __init__(self, rows: int, cols: int, seed: Optional[int] = None):
        self.rows: int = rows
        self.cols: int = cols
        self.maze: List[List[str]] = [['#' for _ in range(cols)] for _ in range(rows)]
        self.start: Tuple[int, int] = (1, 1)
        self.end: Tuple[int, int] = (rows - 2, cols - 2)
        self.start_symbol: str = 'S'
        self.end_symbol: str = 'E'
        if seed is not None:
            random.seed(seed)

    def _is_valid(self, x: int, y: int) -> bool:
        return 0 <= x < self.rows and 0 <= y < self.cols

    def _is_wall(self, x: int, y: int) -> bool:
        return self.maze[x][y] == '#'

    def generate(self) -> None:
        raise NotImplementedError("Subclasses must implement the generate method")

    def print_maze(self) -> None:
        for row in self.maze:
            print(' '.join(row))


class DepthFirstMazeGenerator(MazeGenerator):
    def __init__(self, rows: int, cols: int, seed: Optional[int] = None):
        super().__init__(rows, cols, seed)

    def generate(self, current: Optional[Tuple[int, int]] = None) -> None:
        if current is None:
            current = self.start

        x, y = current
        self.maze[x][y] = ' '

        neighbors = [
            (x + 2, y),
            (x - 2, y),
            (x, y + 2),
            (x, y - 2),
        ]

        # Shuffle the neighbors to get a random order
        random.shuffle(neighbors)

        for neighbor in neighbors:
            nx, ny = neighbor

            if self._is_valid(nx, ny) and self._is_wall(nx, ny):
                wall_x = (x + nx) // 2
                wall_y = (y + ny) // 2

                # Pave the way
                self.maze[wall_x][wall_y] = ' '

                # Recursively call generate with the neighbor
                self.generate(neighbor)

    def generate_maze(self) -> None:
        self.generate()
        self.maze[self.start[0]][self.start[1]] = self.start_symbol
        self.maze[self.end[0]][self.end[1]] = self.end_symbol


if __name__ == "__main__":
    rows: int = 15
    cols: int = 27

    generator = DepthFirstMazeGenerator(rows, cols)
    generator.generate_maze()
    generator.print_maze()
