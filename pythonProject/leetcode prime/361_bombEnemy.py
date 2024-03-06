def count_row_enemies(grid, r, c):
    count = 0
    while c < len(grid[0]) and grid[r][c] != 'W':
        if grid[r][c] == 'E':
            count += 1
        c += 1
    return count


def count_col_enemies(grid, r, c):
    count = 0
    while r < len(grid) and grid[r][c] != 'W':
        if grid[r][c] == 'E':
            count += 1
        r += 1
    return count


def max_killed_enemies(grid):
    if not grid:
        return 0
    rows = len(grid)
    col = len(grid[0])
    max_killed = 0
    row_count = [0] * rows
    col_count = [0] * col
    for r in range(rows):
        for c in range(col):
            if grid[r][c] == 'W':
                continue
            if c == 0 or grid[r][c - 1] == 'W':
                row_count[r] = count_row_enemies(grid, r, c)
            if r == 0 or grid[r - 1][c] == 'W':
                col_count[c] = count_col_enemies(grid, r, c)

    for r in range(rows):
        for c in range(col):
            if grid[r][c] == '0':
                max_killed = max(max_killed, row_count[r] + col_count[c])

    return max_killed


grid = [
    ["0", "E", "0", "0"],
    ["E", "0", "W", "E"],
    ["0", "E", "0", "0"]
]
print(max_killed_enemies(grid))


