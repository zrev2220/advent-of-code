grid = []
guard_x = None
guard_y = None
WIDTH = None
HEIGHT = None

try:
    while True:
        line = input().strip()
        WIDTH = len(line)
        guard_location = line.find("^")
        if guard_location != -1:
            guard_x = guard_location
            guard_y = len(grid)
            line = line.replace("^", ".")
        grid.append(list(line))
except EOFError:
    pass
HEIGHT = len(grid)

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

guard_dir_index = 0
total = 0
while 0 <= guard_x < WIDTH and 0 <= guard_y < HEIGHT:
    if grid[guard_y][guard_x] == ".":
        grid[guard_y][guard_x] = "X"
        total += 1

    next_x = None
    next_y = None
    while next_x is None or next_y is None or grid[next_y][next_x] == "#":
        if next_x is not None or next_y is not None:
            guard_dir_index = (guard_dir_index + 1) % len(dirs)
        guard_dir = dirs[guard_dir_index]
        next_x = guard_x + guard_dir[0]
        next_y = guard_y + guard_dir[1]

        if next_x < 0 or next_x >= WIDTH or next_y < 0 or next_y >= HEIGHT:
            break

    guard_x = next_x
    guard_y = next_y

print(total)
# print(*["".join(row) for row in grid], sep="\n")
