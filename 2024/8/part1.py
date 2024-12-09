from collections import defaultdict
from itertools import combinations

grid = []
nodes = defaultdict(list)

WIDTH = None
try:
    while True:
        line = input().strip()
        WIDTH = len(line)
        grid.append(line)
        for col, char in enumerate(line):
            coords = (col, len(grid) - 1)
            if char != ".":
                nodes[char].append(coords)
except EOFError:
    pass

HEIGHT = len(grid)

antinodes: set[tuple[int, int]] = set()
for frequency, antennas in nodes.items():
    for pair in combinations(antennas, 2):
        a, b = sorted(pair)
        ax, ay = a
        bx, by = b

        for antinode in [
            (
                ax - (bx - ax),
                ay - (by - ay) if by >= ay else ay + (ay - by),
            ),
            (
                bx + (bx - ax),
                by + (by - ay) if by >= ay else by - (ay - by),
            ),
        ]:
            if 0 <= antinode[0] < WIDTH and 0 <= antinode[1] < HEIGHT:
                antinodes.add(antinode)

print(len(antinodes))
