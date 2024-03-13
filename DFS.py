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

def is_traversable(cell, grid, traversable_values):
    return (0 <= cell.x < len(grid)) and (0 <= cell.y < len(grid[0])) and (grid[cell.x][cell.y] in traversable_values)

def dfs(grid):
    traversable_values = [0, 2]
    destination_value = 3

    start = find_positions(grid, 2)
    end = find_positions(grid, 3)

    if not start or not end:
        return None  

    stack = [start]
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    path = []

    while stack:
        current = stack.pop()
        if not visited[current.x][current.y]:
            visited[current.x][current.y] = True

            # If the destination is reached
            if current.x == end.x and current.y == end.y:
                while current:
                    path.append((current.x, current.y))
                    current = current.parent
                return path[::-1]  # Reverse the path

            # Exploring neighbors
            neighbors = [
                Cell(current.x + 1, current.y),
                Cell(current.x - 1, current.y),
                Cell(current.x, current.y + 1),
                Cell(current.x, current.y - 1)
            ]

            for neighbor in neighbors:
                if is_traversable(neighbor, grid, traversable_values) and not visited[neighbor.x][neighbor.y]:
                    neighbor.parent = current
                    stack.append(neighbor)

    return None  # No path found

def main():
    array = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0 ],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],   
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    ]
    
    res = dfs(array)  
    
    if res:
        print("Path found:", res)
    else:
        print("No path found")

if __name__ == "__main__":
    main()
