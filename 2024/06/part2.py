grid = []
init_guard_x = None
init_guard_y = None
WIDTH = None
HEIGHT = None

try:
    while True:
        line = input().strip()
        WIDTH = len(line)
        guard_location = line.find("^")
        if guard_location != -1:
            init_guard_x = guard_location
            init_guard_y = len(grid)
            line = line.replace("^", ".")
        grid.append(list(line))
except EOFError:
    pass
HEIGHT = len(grid)

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# super naive and slow solution, but it gets the job done if you have a minute
#  to wait 🐢
total = 0
for block_y in range(WIDTH):
    for block_x in range(HEIGHT):
        if grid[block_y][block_x] == "#" or (init_guard_y, init_guard_x) == (
            block_y,
            block_x,
        ):
            continue

        temp_grid = [row[:] for row in grid]
        temp_grid[block_y][block_x] = "#"
        guard_x = init_guard_x
        guard_y = init_guard_y

        guard_dir_index = 0
        looping = False
        bonks = set()
        while 0 <= guard_x < WIDTH and 0 <= guard_y < HEIGHT and not looping:
            if temp_grid[guard_y][guard_x] == ".":
                temp_grid[guard_y][guard_x] = "X"

            next_x = None
            next_y = None
            for guard_dir_offset in range(len(dirs)):
                temp_guard_dir_index = (guard_dir_index + guard_dir_offset) % len(dirs)
                guard_dir = dirs[temp_guard_dir_index]
                next_x = guard_x + guard_dir[0]
                next_y = guard_y + guard_dir[1]
                if (
                    next_x < 0
                    or next_x >= WIDTH
                    or next_y < 0
                    or next_y >= HEIGHT
                    or temp_grid[next_y][next_x] != "#"
                ):
                    guard_dir_index = temp_guard_dir_index
                    break
                else:
                    loc = (next_x, next_y, guard_dir)
                    if loc in bonks:
                        looping = True
                        break
                    bonks.add(loc)

            guard_x = next_x
            guard_y = next_y
        if looping:
            total += 1

print(total)
