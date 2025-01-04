from functools import cache
import hashlib

keypad = [
    "789",
    "456",
    "123",
    "#0A",
]

KEYPAD_HEIGHT = len(keypad)
KEYPAD_WIDTH = len(keypad[0])

remote = [
    "#^A",
    "<v>",
]

REMOTE_HEIGHT = len(remote)
REMOTE_WIDTH = len(remote[0])


def make_coord_dict(grid: list[str]) -> dict[str, tuple[int, int]]:
    result = {}
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            result[c] = (i, j)
    return result


keypad_dict = make_coord_dict(keypad)
remote_dict = make_coord_dict(remote)

dirs = {
    "<": (0, -1),
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
}


@cache
def explore(
    pos: tuple[int, int],
    end: tuple[int, int],
    state: tuple[str, ...],
    *,
    is_keypad=False,
) -> int:
    call_hash = hashlib.sha256()
    for s in (str(n) for n in (*pos, *end, is_keypad)):
        call_hash.update(s.encode())
    for s in state:
        call_hash.update(s.encode())
    call_hash_digest = call_hash.hexdigest()

    debug_prefix_call_hash = (
        f"\x1b[38;5;{int(call_hash_digest[-2:], 16)}m{call_hash_digest[-4:]}\x1b[0m"
    )
    debug_prefix_keypad = f"\x1b[{'31mk' if is_keypad else '34mr'}\x1b[0m"
    debug_prefix_state = f"{''.join(state):>{ROBOTS}}"
    debug_prefix = (
        f"{debug_prefix_call_hash}|{debug_prefix_keypad}|{debug_prefix_state}|"
    )

    def debug(*args, **kwargs):
        return  # comment out to enable debug logs
        print(debug_prefix, *args, **kwargs)

    debug(f"\x1b[32mstart\x1b[0m", pos, end, state)
    grid = keypad if is_keypad else remote

    if pos == end:
        debug(f"\x1b[33mending\x1b[0m")
        end_cost = (
            1
            if len(state) == 0
            else explore(remote_dict[state[0]], remote_dict["A"], state[1:])
        )
        debug(f"\x1b[33mended\x1b[0m; {end_cost} to press A")
        # cost to press "A"
        return end_cost

    current_distance = sum(abs(s - e) for s, e in zip(pos, end))
    best: int | None = None
    for keypress, dir in dirs.items():
        next_pos: tuple[int, int] = tuple(map(sum, zip(pos, dir)))
        new_distance = sum(abs(s - e) for s, e in zip(next_pos, end))
        debug(" ", keypress, next_pos, f"{new_distance} vs. {current_distance}")
        if new_distance < current_distance:
            try:
                if grid[next_pos[0]][next_pos[1]] == "#":
                    debug("  hash crash")
                    continue
            except IndexError:
                debug("  oob crash")
                continue
            debug(f"    \x1b[1;34mgo\x1b[0m {keypress} from {pos} to {next_pos}")
            keypress_cost = (
                1
                if len(state) == 0
                else explore(remote_dict[state[0]], remote_dict[keypress], state[1:])
            )
            remaining_path_cost = explore(
                next_pos,
                end,
                (keypress,) + state[1:] if len(state) > 0 else tuple(),
                is_keypad=is_keypad,
            )
            cost = keypress_cost + remaining_path_cost
            debug(f"    \x1b[1;34mwent\x1b[0m {keypress} from {pos} to {next_pos} ")
            debug(f"         {keypress_cost=} {remaining_path_cost=}")
            if best is None or cost < best:
                best = cost
    debug(f"\x1b[1;32m{best=}\x1b[0m for {pos} to {end}")
    return best


ROBOTS = 25

codes = [input().strip() for _ in range(5)]

total = 0
for code in codes:
    print(f"===== {code} =====")
    last_digit = "A"
    code_total = 0
    for digit in code:
        digit_total = explore(
            keypad_dict[last_digit], keypad_dict[digit], ("A",) * ROBOTS, is_keypad=True
        )
        print(f"{last_digit} -> {digit} = {digit_total}")
        code_total += digit_total
        last_digit = digit
    print(code_total)
    total += code_total * int(code[:-1])
print(total)
cache_info = explore.cache_info()
print(f"{cache_info.hits / (cache_info.hits + cache_info.misses):0.2}", cache_info)
