word = "XMAS"

grid = []
try:
    while True:
        line = input().strip()
        if line:
            grid.append(line)
except EOFError:
    pass


def explore(grid, i, j) -> int:
    if grid[i][j] != word[0]:
        return 0
    result = 0
    for xdir in [-1, 0, 1]:
        for ydir in [-1, 0, 1]:
            valid = True
            for c in range(1, len(word)):
                new_i = i + ydir * c
                new_j = j + xdir * c
                if (
                    new_i < 0
                    or new_j < 0
                    or new_i >= len(grid)
                    or new_j >= len(grid[new_i])
                    or grid[new_i][new_j] != word[c]
                ):
                    valid = False
                    break
            if valid:
                result += 1
    return result


total = 0
for i in range(len(grid)):
    row = grid[i]
    for j in range(len(row)):
        total += explore(grid, i, j)
print(total)
