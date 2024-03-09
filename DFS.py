class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

def find_positions(array, x):
    for i, row in enumerate(array):
        for j, element in enumerate(row):
            if element == x:
                return Cell(i, j)
    return None

def is_valid(cell, array):
    return (0 <= cell.x < len(array)) and (0 <= cell.y < len(array[0])) and (array[cell.x][cell.y] != 1)

def dfs(array):
    start = find_positions(array, 2)  # Find start position
    end = find_positions(array, 3)    # Find end position

    if not start or not end:
        return None  # If start or end is not found

    stack = [start]
    visited = [[False for _ in range(len(array[0]))] for _ in range(len(array))]
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
                if is_valid(neighbor, array) and not visited[neighbor.x][neighbor.y]:
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
    res = dfs(array)  # Call dfs with only the array
    if res:
        print("Path found:", res)
    else:
        print("No path found")

if __name__ == "__main__":
    main()
