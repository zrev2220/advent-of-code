def recurse(value, goal, operands) -> bool:
    if not operands:
        return value == goal
    current, rest = operands[0], operands[1:]
    return (
        recurse(value + current, goal, rest)
        or recurse(value * current, goal, rest)
        or recurse(int(str(value) + str(current)), goal, rest)
    )


result = 0
try:
    while True:
        line = input().strip()
        goal_raw, operands_raw = map(lambda s: s.strip(), line.split(":"))
        goal = int(goal_raw)
        operands = list(map(int, operands_raw.split()))
        if recurse(operands[0], goal, operands[1:]):
            result += goal
except EOFError:
    pass

print(result)
