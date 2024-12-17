import re
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw
from tqdm import tqdm


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
TIME = 100000

# draw the robots at every second for...quite a while
# then open the folder in file viewer and go looking for a Christmas tree

# I could probably instead filter to only cases where the majority of the grid
# is empty
debug_folder = "part2-debug"
Path(debug_folder).mkdir(exist_ok=True)

for second in tqdm(range(TIME + 1)):
    with Image.new("RGB", (WIDTH, HEIGHT), "#fff") as image:
        draw = ImageDraw.Draw(image)
        for robot in robots:
            x, y = robot.position
            dx, dy = robot.velocity

            new_x = (x + dx * second) % WIDTH
            new_y = (y + dy * second) % HEIGHT
            draw.point([(new_x, new_y)], fill="#000")

        image.save(f"{debug_folder}/{second:03}.png")
