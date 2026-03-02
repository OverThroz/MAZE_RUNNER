import random

def generate_maze(width, height):
    # Initialize grid full of walls
    maze = [[1 for _ in range(width)] for _ in range(height)]

    # Starting point
    start_x, start_y = 1, 1
    maze[start_y][start_x] = 0

    # Directions: N, S, E, W (dy, dx)
    directions = [(-2, 0), (2, 0), (0, 2), (0, -2)]

    def carve(x, y):
        random.shuffle(directions)
        for dy, dx in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width-1 and 1 <= ny < height-1:
                if maze[ny][nx] == 1:
                    maze[ny][nx] = 0
                    maze[y + dy//2][x + dx//2] = 0  # carve the wall between
                    carve(nx, ny)

    carve(start_x, start_y)

    # Place exit at bottom right open cell
    for i in range(width-2, 0, -1):
        for j in range(height-2, 0, -1):
            if maze[j][i] == 0:
                maze[j][i] = 2
                return maze

    return maze
