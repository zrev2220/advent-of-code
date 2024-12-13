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


def flood(coords) -> int:
    area = 0
    perimeter = 0
    color = grid[coords[0]][coords[1]]
    visited.add(coords)
    queue = [coords]
    while queue:
        i, j = queue.pop(0)
        area += 1
        for j_dir, i_dir in [
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, 0),
        ]:
            i2 = i + i_dir
            j2 = j + j_dir
            if i2 < 0 or i2 >= HEIGHT or j2 < 0 or j2 >= WIDTH or grid[i2][j2] != color:
                perimeter += 1
            elif grid[i2][j2] == color and (i2, j2) not in visited:
                visited.add((i2, j2))
                queue.append((i2, j2))
    return area * perimeter


price = 0
for i in range(HEIGHT):
    for j in range(WIDTH):
        loc = (i, j)
        if loc not in visited:
            price += flood(loc)
print(price)
