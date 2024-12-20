from collections import defaultdict

TESTING = False

SIZE = 7 if TESTING else 71

block_list: list[tuple[int, int]] = []
try:
    while True:
        block_list.append(tuple(map(int, input().strip().split(","))))
except EOFError:
    pass

dirs = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

# binary search the block that ends it all
hi = len(block_list) - 1
lo = 0
while lo < hi:
    mid = (lo + hi) // 2

    blocks = set(block_list[: mid + 1])
    end = (SIZE - 1, SIZE - 1)
    queue = [(0, 0)]
    visited = set()
    distance = defaultdict[tuple[int, int], int | None](lambda: None)
    distance[(0, 0)] = 0
    parent = defaultdict[tuple[int, int], tuple[int, int] | None](lambda: None)
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
                    parent[(i2, j2)] = (i, j)
                queue.append((i2, j2))
        visited.add((i, j))

    path = {end}
    p = parent[end]
    while p:
        path.add(p)
        p = parent[p]

    if distance[end] == None:
        hi = mid
    else:
        lo = mid + 1
print(*block_list[lo], sep=",")
