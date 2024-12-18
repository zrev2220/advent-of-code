import time

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
            line = (
                line.replace("#", "##")
                .replace(".", "..")
                .replace("@", "@.")
                .replace("O", "[]")
            )
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


moved = set[tuple[int, int]]()


def check_shove(
    coords: tuple[int, int], dir: str, *, ignore_moving: bool = False
) -> list[tuple[int, int]] | None:
    i, j = coords
    if grid[i][j] == "]":
        j -= 1
    if not ignore_moving and moved.intersection(((i, j), (i, j + 1))):
        return []
    moved.update(((i, j), (i, j + 1)))
    di, dj = dirs[dir]
    i2 = i + di
    j2 = j + dj
    j22 = j2 + 1
    if dir == ">":
        j2 += 1
        j22 += 1

    if (
        i2 < 0
        or i2 >= HEIGHT
        or j2 < 0
        or j22 >= WIDTH
        or grid[i2][j2] == "#"
        or (dir != ">" and grid[i2][j22] == "#")
    ):
        return None
    elif (dir == ">" and grid[i2][j2] == "[") or (dir == "<" and grid[i2][j2] == "]"):
        child_shove = check_shove((i2, j2), dir)
        if child_shove is None:
            return None
        return [(i, j), *child_shove]
    elif dir in "^v" and (grid[i2][j2] in "[]" or grid[i2][j22] in "[]"):
        child_shove1 = check_shove((i2, j2), dir) if grid[i2][j2] in "[]" else []
        child_shove2 = check_shove((i2, j22), dir) if grid[i2][j22] in "[]" else []
        if child_shove1 is None or child_shove2 is None:
            return None
        return [(i, j), *child_shove2, *child_shove1]

    return [(i, j)]


def shove(to_shove: list[tuple[int, int]], dir: str):
    while to_shove:
        i, j = to_shove.pop()
        di, dj = dirs[dir]
        i2 = i + di
        j2 = j + dj
        grid[i][j] = grid[i][j + 1] = "."
        grid[i2][j2] = "["
        grid[i2][j2 + 1] = "]"


for m, move in enumerate(movements):
    i, j = robot
    di, dj = dirs[move]
    i2 = i + di
    j2 = j + dj
    can_move = True
    moved.clear()
    if i2 < 0 or i2 >= HEIGHT or j2 < 0 or j2 >= WIDTH or grid[i2][j2] == "#":
        can_move = False
    elif grid[i2][j2] in "[]":
        to_shove = check_shove((i2, j2), move, ignore_moving=True)
        if to_shove is None:
            can_move = False
        else:
            shove(to_shove, move)
    if can_move:
        robot = (i2, j2)


total = 0
for i, row in enumerate(grid):
    for j, c in enumerate(row):
        if c == "[":
            total += 100 * i + j
print(total)
