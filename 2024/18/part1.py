from collections import defaultdict

TESTING = False

SIZE = 7 if TESTING else 71
LIMIT = 12 if TESTING else 1024

blocks = set[tuple[int, int]]()
try:
    while True:
        blocks.add(tuple(map(int, input().strip().split(","))))
        if len(blocks) >= LIMIT:
            break
except EOFError:
    pass

dirs = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

end = (SIZE - 1, SIZE - 1)
queue = [(0, 0)]
visited = set()
distance = defaultdict[tuple[int, int], int | None](lambda: None)
distance[(0, 0)] = 0
while queue:
    i, j = queue.pop(0)
    if (i, j) in visited or (i, j) == end:
        continue
    current_distance = distance[(i, j)]
    for di, dj in dirs:
        i2 = i + di
        j2 = j + dj
        if 0 <= i2 < SIZE and 0 <= j2 < SIZE and (i2, j2) not in blocks:
            existing_distance = distance[(i2, j2)]
            if (
                existing_distance is None
                or current_distance + 1 < existing_distance
            ):
                distance[(i2, j2)] = current_distance + 1
            queue.append((i2, j2))
    visited.add((i, j))
print(distance[end])
