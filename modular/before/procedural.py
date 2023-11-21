import random


def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    start = (1, 1)
    end = (rows - 2, cols - 2)

    stack = [start]
    visited = set()

    while stack:
        current = stack[-1]
        x, y = current

        maze[x][y] = ' '
        visited.add(current)

        neighbors = [
            (x + 2, y),
            (x - 2, y),
            (x, y + 2),
            (x, y - 2),
        ]

        unvisited_neighbors = [neighbor for neighbor in neighbors if
                               is_valid(neighbor[0], neighbor[1], rows, cols) and neighbor not in visited]

        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            nx, ny = next_cell

            wall_x = (x + nx) // 2
            wall_y = (y + ny) // 2
            maze[wall_x][wall_y] = ' '

            stack.append(next_cell)
        else:
            stack.pop()

    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'

    return maze


def print_maze(maze):
    for row in maze:
        print(' '.join(row))


if __name__ == "__main__":
    rows = 11
    cols = 21

    maze = generate_maze(rows, cols)
    print_maze(maze)
