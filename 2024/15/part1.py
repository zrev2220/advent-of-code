grid = []
WIDTH = None
movements = []

dirs = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

reading_movements = False
robot = None
try:
    while True:
        line = input().strip()
        if line == "":
            reading_movements = True
            continue
        elif not reading_movements:
            WIDTH = len(line)
            possible_start = line.find("@")
            if possible_start != -1:
                robot = (len(grid), possible_start)
                line = line.replace("@", ".")
            grid.append(list(line))
        else:
            movements.extend(list(line))
except EOFError:
    pass
HEIGHT = len(grid)


def shove(coords: tuple[int, int], dir: tuple[int, int]) -> bool:
    i, j = coords
    di, dj = dir
    i2 = i + di
    j2 = j + dj
    can_move = True
    if i2 < 0 or i2 >= HEIGHT or j2 < 0 or j2 >= WIDTH or grid[i2][j2] == "#":
        can_move = False
    elif grid[i2][j2] == "O":
        can_move = shove((i2, j2), dir)
    if can_move:
        grid[i][j] = "."
        grid[i2][j2] = "O"
    return can_move


for move in movements:
    i, j = robot
    di, dj = dirs[move]
    i2 = i + di
    j2 = j + dj
    can_move = True
    if i2 < 0 or i2 >= HEIGHT or j2 < 0 or j2 >= WIDTH or grid[i2][j2] == "#":
        continue
    elif grid[i2][j2] == "O":
        can_move = shove((i2, j2), (di, dj))
    if can_move:
        robot = (i2, j2)


total = 0
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "O":
            total += 100 * i + j
print(total)
