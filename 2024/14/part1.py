import re
from collections import defaultdict
from dataclasses import dataclass
from functools import reduce


@dataclass
class Robot:
    position: tuple[int, int]
    velocity: tuple[int, int]


robots = []
try:
    while True:
        px, py, vx, vy = map(
            int,
            re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", input().strip()).groups(),
        )
        robots.append(Robot(position=(px, py), velocity=(vx, vy)))
except EOFError:
    pass

WIDTH = 101
HEIGHT = 103
# WIDTH = 11
# HEIGHT = 7
TIME = 100
quadrants = defaultdict(int)
for robot in robots:
    x, y = robot.position
    dx, dy = robot.velocity

    new_x = (x + dx * TIME) % WIDTH
    new_y = (y + dy * TIME) % HEIGHT

    q = None
    if new_x < WIDTH // 2 and new_y < HEIGHT // 2:
        q = 1
    elif new_x < WIDTH // 2 and new_y > HEIGHT // 2:
        q = 2
    elif new_x > WIDTH // 2 and new_y < HEIGHT // 2:
        q = 3
    elif new_x > WIDTH // 2 and new_y > HEIGHT // 2:
        q = 4
    if q is not None:
        quadrants[q] += 1

print(reduce(lambda a, b: a * b, quadrants.values(), 1))
