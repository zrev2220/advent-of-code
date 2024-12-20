from collections import defaultdict

grid = []
WIDTH = None

start: tuple[int, int] = None
end: tuple[int, int] = None
try:
    while True:
        line = input().strip()
        WIDTH = len(line)
        possible_start = line.find("S")
        if possible_start != -1:
            start = (len(grid), possible_start)
        possible_end = line.find("E")
        if possible_end != -1:
            end = (len(grid), possible_end)

        grid.append(line)
except EOFError:
    pass
HEIGHT = len(grid)

dirs = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

# bfs backwards from end to establish distances
queue = [end]
visited = set()
distance = defaultdict[tuple[int, int], int | None](lambda: None)
distance[end] = 0
while queue:
    i, j = queue.pop(0)
    if (i, j) in visited:
        continue
    current_distance = distance[(i, j)]
    for di, dj in dirs:
        i2 = i + di
        j2 = j + dj
        if 0 <= i2 < HEIGHT and 0 <= j2 < WIDTH and grid[i2][j2] != "#":
            existing_distance = distance[(i2, j2)]
            if existing_distance is None or current_distance + 1 < existing_distance:
                distance[(i2, j2)] = current_distance + 1
            queue.append((i2, j2))
    visited.add((i, j))

# bfs forwards from start, bfs'ing *again* from each space while cheating to see how much we can save
MAX_CHEAT = 20
CHEAT_THRESHOLD = 100
# CHEAT_THRESHOLD = 50
visited = set()
queue = [start]
result = 0
cheat_log = defaultdict[int, set[tuple[tuple[int, int], tuple[int, int]]]](set)


def get_cheats(
    start: tuple[int, int]
) -> dict[tuple[tuple[int, int], tuple[int, int]], int]:
    result = 0
    visited = set()
    queue = [start]
    cheats: dict[tuple[tuple[int, int], tuple[int, int]], int] = {}
    while queue:
        i, j = queue.pop(0)
        if (i, j) in visited:
            continue

        for di, dj in dirs:
            i2 = i + di
            j2 = j + dj
            cheat_length = abs(start[0] - i2) + abs(start[1] - j2)
            if 0 <= i2 < HEIGHT and 0 <= j2 < WIDTH:
                if cheat_length < MAX_CHEAT:
                    # we don't have to stop the cheat yet
                    queue.append((i2, j2))
                if grid[i2][j2] != "#":
                    # get efficacy if we stop the cheat here
                    efficacy = distance[start] - distance[(i2, j2)] - cheat_length
                    if efficacy >= CHEAT_THRESHOLD:
                        result += 1
                        cheats[(start, (i2, j2))] = efficacy
        visited.add((i, j))
    return cheats


while queue:
    i, j = queue.pop(0)
    if (i, j) in visited or (i, j) == end:
        continue

    cheats = get_cheats((i, j))
    result += len(cheats)
    for cheat, efficacy in cheats.items():
        cheat_log[efficacy].add(cheat)

    for di, dj in dirs:
        i2 = i + di
        j2 = j + dj
        if 0 <= i2 < HEIGHT and 0 <= j2 < WIDTH and grid[i2][j2] != "#":
            queue.append((i2, j2))
    visited.add((i, j))
print(result)
