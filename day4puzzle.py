# --- Day 4: Paper Roll Removal ---

with open("day4input.txt", "r") as f:
    lines = f.read().splitlines()

grid = [list(line) for line in lines]
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

def count_adjacent(i, j, grid, rows, cols, directions):
    return sum(
        1 for di, dj in directions
        if 0 <= i + di < rows and 0 <= j + dj < cols
        and grid[i + di][j + dj] == '@'
    )

accessible_count = sum(
    1 for i in range(rows)
    for j in range(cols)
    if grid[i][j] == '@' and count_adjacent(i, j, grid, rows, cols, directions) < 4
)

print(f"part 1: {accessible_count}")


with open("day4input.txt", "r") as f:
    lines = f.read().splitlines()
    grid = [list(line) for line in lines]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

total_removed = 0
while True:
    to_remove = [
        (i, j) for i in range(rows) for j in range(cols)
        if grid[i][j] == '@' and count_adjacent(i, j, grid, rows, cols, directions) < 4
    ]
    
    if len(to_remove) == 0:
        break
    
    for i, j in to_remove:
        grid[i][j] = 'x'
    
    total_removed += len(to_remove)

print(f"part 2: {total_removed}")
