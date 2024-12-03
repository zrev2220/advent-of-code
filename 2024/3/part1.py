import re

total = 0
try:
    while True:
        line = input()
        for match in re.finditer(r"mul\((?P<x>\d+),(?P<y>\d+)\)", line):
            x = int(match.group("x"))
            y = int(match.group("y"))
            total += x * y
except EOFError:
    pass

print(total)
