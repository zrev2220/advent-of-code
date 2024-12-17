import re
from collections import defaultdict


A_COST = 3
B_COST = 1

first = True
total = 0
try:
    while True:
        if first:
            first = False
        else:
            input()
        ax, ay = map(
            int, re.match(r"Button A: X\+(\d+), Y\+(\d+)", input().strip()).groups()
        )
        bx, by = map(
            int, re.match(r"Button B: X\+(\d+), Y\+(\d+)", input().strip()).groups()
        )
        prize_x, prize_y = map(
            int, re.match(r"Prize: X=(\d+), Y=(\d+)", input().strip()).groups()
        )

        # it's kinda dumb and a bit slow but I'm solving this using Dijkstra's
        # 'cuz it's fun
        # (I'll break out linear algebra for part 2)
        queue = [(0, 0)]
        visited = set()
        distance = defaultdict[tuple[int, int], int | None](lambda: None)
        distance[(0, 0)] = 0
        while queue:
            x, y = queue.pop(0)
            if (x, y) in visited:
                continue
            current_distance = distance[(x, y)]
            for button_cost, dx, dy in [(A_COST, ax, ay), (B_COST, bx, by)]:
                new_x = x + dx
                new_y = y + dy
                if (
                    new_x <= prize_x
                    and new_y <= prize_y
                    and (new_x, new_y) not in visited
                ):
                    existing_distance = distance[(new_x, new_y)]
                    if (
                        existing_distance is None
                        or current_distance + button_cost < existing_distance
                    ):
                        distance[(new_x, new_y)] = current_distance + button_cost
                    queue.append((new_x, new_y))
            visited.add((x, y))
        total += distance[(prize_x, prize_y)] or 0
except EOFError:
    pass
print(total)
