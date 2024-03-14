class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

def find_positions(grid, value):
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element == value:
                return Cell(i, j)
    return None

def is_traversable(x, y, grid, visited):
    if (x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1) and grid[x][y] == 0:
        return False
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y] and grid[x][y] != 1

def dfs_internal(grid, start, end, visited):
    if start.x == end.x and start.y == end.y:
        path = []
        while start:
            path.append((start.x, start.y))
            start = start.parent
        return path[::-1]

    visited[start.x][start.y] = True

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = start.x + dx, start.y + dy
        if is_traversable(nx, ny, grid, visited):
            next_cell = Cell(nx, ny)
            next_cell.parent = start
            result = dfs_internal(grid, next_cell, end, visited)
            if result:
                return result

    return None

def dfs(grid):
    start = find_positions(grid, 2)
    end = find_positions(grid, 3)
    if not start or not end:
        return None

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    return dfs_internal(grid, start, end, visited)