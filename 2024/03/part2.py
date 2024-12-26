import re

total = 0
enabled = True
try:
    while True:
        line = input()
        for match in re.finditer(
            r"(mul\((?P<x>\d+),(?P<y>\d+)\)|don't\(\)|do\(\))", line
        ):
            str_match = match[0]
            if str_match.startswith("don't"):
                enabled = False
            elif str_match.startswith("do"):
                enabled = True
            elif enabled:
                x = int(match["x"])
                y = int(match["y"])
                total += x * y
except EOFError:
    pass

print(total)
