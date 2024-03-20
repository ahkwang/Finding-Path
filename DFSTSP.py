import itertools
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

def is_traversable(cell, grid):
    if cell.x == 0 or cell.x == len(grid) - 1 or cell.y == 0 or cell.y == len(grid[0]) - 1:
        if grid[cell.x][cell.y] == 0:
            return False
    return (0 <= cell.x < len(grid)) and (0 <= cell.y < len(grid[0])) and (grid[cell.x][cell.y] != 1)

def trace_path(cell):
    path = []
    while cell:
        path.append((cell.x, cell.y))
        cell = cell.parent
    path.reverse()
    return path

def dfs(grid, start, end):
    if not start or not end:
        return None  

    stack = [start]
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    path = []

    while stack:
        current = stack.pop()
        if visited[current.x][current.y]:
            continue
        visited[current.x][current.y] = True

        if current.x == end.x and current.y == end.y:
            return trace_path(current)

        neighbors = [
            Cell(current.x + 1, current.y), Cell(current.x - 1, current.y),
            Cell(current.x, current.y + 1), Cell(current.x, current.y - 1),
        ]

        for neighbor in neighbors:
            if is_traversable(neighbor, grid) and not visited[neighbor.x][neighbor.y]:
                neighbor.parent = current
                stack.append(neighbor)

    return None  

def find_pickup_points(grid):
    return [Cell(x, y) for x, row in enumerate(grid) for y, value in enumerate(row) if value == 4]

def dfsTSP(grid):
    start = find_positions(grid, 2)
    end = find_positions(grid, 3)
    pickup_points = find_pickup_points(grid)

    all_permutations = itertools.permutations(pickup_points)
    shortest_path = None
    shortest_path_length = float('inf')

    for permutation in all_permutations:
        current_path = []
        current_length = 0
        current_point = start
        for next_point in permutation:
            path_segment = dfs(grid, current_point, next_point)
            if not path_segment:
                break  
            current_path.extend(path_segment if current_point == start else path_segment[1:])
            current_length += len(path_segment) - 1
            current_point = next_point
        else:
            path_to_end = dfs(grid, current_point, end)
            if path_to_end:
                current_path.extend(path_to_end if current_point == start else path_to_end[1:])
                current_length += len(path_to_end) - 1
                if current_length < shortest_path_length:
                    shortest_path_length = current_length
                    shortest_path = current_path

    return shortest_path