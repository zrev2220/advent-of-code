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

# bfs forwards from start, testing each cheat possibility to see how much time it saves
CHEAT_THRESHOLD = 100
visited = set()
queue = [start]
cheats = 0
while queue:
    i, j = queue.pop(0)
    if (i, j) in visited or (i, j) == end:
        continue
    for di, dj in dirs:
        i2 = i + di
        j2 = j + dj
        i3 = i + di * 2
        j3 = j + dj * 2
        if 0 <= i2 < HEIGHT and 0 <= j2 < WIDTH and grid[i2][j2] != "#":
            queue.append((i2, j2))
        elif 0 <= i3 < HEIGHT and 0 <= j3 < WIDTH and grid[i3][j3] != "#":
            efficacy = distance[(i, j)] - distance[(i3, j3)] - 2
            if efficacy >= CHEAT_THRESHOLD:
                cheats += 1
    visited.add((i, j))
print(cheats)
