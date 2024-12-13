grid = []
WIDTH = None

try:
    while True:
        line = input().strip()
        WIDTH = len(line)
        grid.append(list(line))
except EOFError:
    pass
HEIGHT = len(grid)

visited = set()


dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


def flood(coords) -> int:
    area = 0
    side_nodes: dict[tuple[int, int, int], tuple[int, int, int] | None] = {}
    color = grid[coords[0]][coords[1]]
    visited.add(coords)
    queue = [coords]
    while queue:
        i, j = queue.pop(0)
        area += 1
        for d, (j_dir, i_dir) in enumerate(dirs):
            i2 = i + i_dir
            j2 = j + j_dir
            if i2 < 0 or i2 >= HEIGHT or j2 < 0 or j2 >= WIDTH or grid[i2][j2] != color:
                side_nodes[(d, i2, j2)] = None
            elif grid[i2][j2] == color and (i2, j2) not in visited:
                visited.add((i2, j2))
                queue.append((i2, j2))

    # combine side nodes to get # of sides

    def find(node):
        parent = side_nodes[node]
        if parent is None:
            return node
        root = find(parent)
        if node != root:
            side_nodes[node] = root
        return root

    def union(a, b):
        a_root = find(a)
        b_root = find(b)
        if a_root != b_root:
            side_nodes[b] = a_root

    for node in side_nodes.keys():
        d, i, j = node
        for i_dir, j_dir in dirs[d % 2 :: 2]:
            i2 = i + i_dir
            j2 = j + j_dir
            adjacent_node = (d, i2, j2)
            if adjacent_node in side_nodes:
                union(adjacent_node, node)

    n_sides = sum(1 for parent in side_nodes.values() if parent is None)
    return area * n_sides


price = 0
for i in range(HEIGHT):
    for j in range(WIDTH):
        loc = (i, j)
        if loc not in visited:
            price += flood(loc)
print(price)
