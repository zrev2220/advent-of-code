from itertools import product

locks = []
keys = []

WIDTH = 5
HEIGHT = 7

try:
    grid = []
    while True:
        first_line = input().strip()
        is_lock = first_line == "#" * WIDTH
        collapsed = tuple(1 if c == "#" else 0 for c in first_line)
        for i in range(1, HEIGHT):
            collapsed = tuple(
                map(
                    sum, zip(collapsed, (1 if c == "#" else 0 for c in input().strip()))
                )
            )
        if is_lock:
            locks.append(collapsed)
        else:
            keys.append(collapsed)

        input()
except EOFError:
    pass

print(
    sum(
        1 if all(item <= HEIGHT for item in map(sum, zip(key, lock))) else 0
        for key, lock in product(keys, locks)
    )
)
