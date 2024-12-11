from dataclasses import dataclass


@dataclass
class Result:
    ends: set[tuple[int, int]]
    paths: int

    def __add__(self, other):
        self.paths += other.paths
        self.ends |= other.ends
        return self


grid = []

WIDTH = None
try:
    while True:
        line = input().strip()
        WIDTH = len(line)
        grid.append(list(map(int, line)))
except EOFError:
    pass
HEIGHT = len(grid)

# I probably don't need DP for this but I'll feel cool if I use it
memo: dict[tuple[int, int], Result] = {}


def hike(coords, depth) -> Result:
    if coords in memo:
        return memo[coords]

    i, j = coords
    cur_loc = grid[i][j]
    if cur_loc == 9:
        result = memo[coords] = Result({coords}, 1)
        return result

    result = Result(set(), 0)
    for i_dir, j_dir in [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1],
    ]:
        i2 = i + i_dir
        j2 = j + j_dir
        if i2 < 0 or i2 >= HEIGHT or j2 < 0 or j2 >= WIDTH:
            continue

        next_loc = grid[i2][j2]
        if next_loc == cur_loc + 1:
            result += hike((i2, j2), depth + 1)
    memo[coords] = result
    return result


score = 0
result = Result(set(), 0)
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == 0:
            hike_result = hike((i, j), 0)
            result += hike_result
            score += len(hike_result.ends)

print(
    f"""\
trailheads:       {len(result.ends)}
total score (p1): {score}
paths (p2):       {result.paths}
"""
)
