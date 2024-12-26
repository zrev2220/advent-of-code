"""
four X-MAS options
M.S  M.M  S.M  S.S
.A.  .A.  .A.  .A.
M.S  S.S  S.M  M.M
"""

xpos = [
    [0, 0],
    [0, 2],
    [1, 1],
    [2, 0],
    [2, 2],
]
mas_options = [
    "MSAMS",
    "MMASS",
    "SMASM",
    "SSAMM",
]
x_width = 3

grid = []
try:
    while True:
        line = input().strip()
        if line:
            grid.append(line)
except EOFError:
    pass


def explore(grid, i, j) -> bool:
    current_x = ""
    for y_dir, x_dir in xpos:
        current_x += grid[i + y_dir][j + x_dir]
    return any([current_x == good_option for good_option in mas_options])


total = 0
for i in range(len(grid) - x_width + 1):
    row = grid[i]
    for j in range(len(row) - x_width + 1):
        if explore(grid, i, j):
            total += 1
print(total)
