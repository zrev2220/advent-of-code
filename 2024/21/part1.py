keypad = [
    "789",
    "456",
    "123",
    "#0A",
]

HEIGHT = len(keypad)
WIDTH = len(keypad[0])

remote = [
    "#^A",
    "<v>",
]

# keypad 3 inputs required to accomplish keypad 2 inputs
# mapped by desired keypad 2 input, by current keypad 2 position
# values are essentially the costs of moving around keypad 1
paths = {
    # current
    "A": {
        # desired
        "A": "A",
        "^": "<A",
        ">": "vA",
        "v": "v<A",
        "<": "v<<A",
    },
    "^": {
        "A": ">A",
        "^": "A",
        ">": "v>A",
        "v": "vA",
        "<": "v<A",
    },
    ">": {
        "A": "^A",
        "^": "<^A",
        ">": "A",
        "v": "<A",
        "<": "<<A",
    },
    "v": {
        "A": "^>A",
        "^": "^A",
        ">": ">A",
        "v": "A",
        "<": "<A",
    },
    "<": {
        "A": ">>^A",
        "^": ">^A",
        ">": ">>A",
        "v": ">A",
        "<": "A",
    },
}


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


def reverse(inputs: str):
    i, j = remote_dict["A"]
    output = ""
    for c in inputs:
        if c == "A":
            output += remote[i][j]
        else:
            di, dj = dirs[c]
            i += di
            j += dj
    return output


def debug_reverse_path(path3: str):
    path2 = reverse(path3)
    path1 = reverse(path2)
    steps = []
    path2_split = path2.replace("A", "A|").split("|")[:-1]
    path3_split = path3.replace("A", "A|").split("|")[:-1]
    offset = 0
    for step, path2_steps in zip(path1, path2_split):
        path3_steps_list = path3_split[offset : offset + len(path2_steps)]
        offset += len(path2_steps)
        steps.append((step, path2_steps, path3_steps_list))
    path1_str = ""
    path2_str = ""
    path3_str = ""
    count_10s_str = ""
    count_str = ""
    counter = 0
    for steps1, steps2, steps3 in steps:
        path1_str += f"{steps1:{4*len(steps2)+len(steps2)-1}}|"
        path2_str += "".join(f"{s:4}|" for s in steps2)
        path3_str += "".join(f"{s:4}|" for s in steps3)
        for s in steps3:
            for i in range(4):
                count_10s_str += f"{(i + counter) // 10}" if i < len(s) else " "
                count_str += f"{(i + counter) % 10}" if i < len(s) else " "
            count_10s_str += "|"
            count_str += "|"
            counter += len(s)
    print(
        f"""\
{len(path1)=}
{len(path2)=}
{len(path3)=}
path1=|{path1_str}
path2=|{path2_str}
path3=|{path3_str}
count=|{count_10s_str}
count=|{count_str}"""
    )


def get_cost(dir: str, keypad2_current: str) -> tuple[int, str]:
    keypad2_path = paths[keypad2_current][dir]
    keypad3_path_elements = []
    prev = "A"
    for step in keypad2_path:
        keypad3_path_elements.append(paths[prev][step])
        prev = step
    keypad3_path = "".join(keypad3_path_elements)
    # print(f"..... from={keypad2_current} go={dir} {keypad2_path=} {keypad3_path=}")
    return len(keypad3_path), keypad3_path


def explore(
    pos: tuple[int, int], end: tuple[int, int], last_keypad2: str
) -> tuple[tuple[int, str]]:
    if pos == end:
        return (get_cost("A", last_keypad2),)

    current_distance = sum(abs(s - e) for s, e in zip(pos, end))
    paths = []
    for keypress, dir in dirs.items():
        next_pos: tuple[int, int] = tuple(map(sum, zip(pos, dir)))
        new_distance = sum(abs(s - e) for s, e in zip(next_pos, end))
        try:
            if keypad[next_pos[0]][next_pos[1]] == "#":
                continue
        except IndexError:
            continue
        if new_distance < current_distance:
            cost, path = get_cost(keypress, last_keypad2)
            paths.extend(
                map(
                    lambda result: (cost + result[0], path + result[1]),
                    explore(next_pos, end, keypress),
                )
            )
    return tuple(paths)


def find_code_path(code: str) -> tuple[int, str]:
    last_digit = "A"
    total = 0
    total_path = ""
    for digit in code:
        distance, path = min(
            explore(keypad_dict[last_digit], keypad_dict[digit], "A"),
            key=lambda result: result[0],
        )
        total += distance
        total_path += path
        last_digit = digit
    return total, total_path


codes = [input().strip() for _ in range(5)]

total = 0
for code in codes:
    print(f"===== {code} =====")
    distance, path = find_code_path(code)
    print(distance)
    total += distance * int(code[:-1])
    # debug_reverse_path(path)
print(total)
