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
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
]
opposite_dirs = [2, 3, 0, 1]
start_dir = 0

queue: list[tuple[int, int, int]] = [(*start, start_dir)]
visited = set()
distance = defaultdict[tuple[int, int, int], int | None](lambda: None)
parent = defaultdict[tuple[int, int, int], tuple[int, int, int] | None](lambda: None)
distance[(*start, start_dir)] = 0

move_cost = 1
turn_cost = 1000

while queue:
    current = queue.pop(0)
    i, j, current_dir = current
    if current in visited or (i, j) == end:
        continue
    current_distance = distance[current]
    for dir, (di, dj) in enumerate(dirs):
        if dir == opposite_dirs[current_dir]:
            continue
        new_i = i + di
        new_j = j + dj
        if 0 <= new_i < HEIGHT and 0 <= new_j < WIDTH and grid[new_i][new_j] != "#":
            next_pos = (new_i, new_j, dir)
            existing_distance = distance[next_pos]
            turns = 0 if dir == current_dir else 1
            cost = move_cost + turns * turn_cost
            if existing_distance is None or current_distance + cost < existing_distance:
                distance[next_pos] = current_distance + cost
                parent[next_pos] = current
                visited.discard(next_pos)
            queue.append(next_pos)
    visited.add(current)

shortest_end = min(
    filter(
        lambda k: distance[k] is not None, [(*end, dir) for dir in range(len(dirs))]
    ),
    key=lambda k: distance[k],
)

print(distance[shortest_end])
